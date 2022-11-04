import requests
from bs4 import BeautifulSoup
import pandas as pd
from concurrent.futures import ThreadPoolExecutor


class amfiIndia:
    def __init__(self) -> None:
        self.cityList = []
        self.output = []

    def getCityList(self):
        resp = requests.get('https://www.amfiindia.com/locate-your-nearest-mutual-fund-distributor-details')
        soup = BeautifulSoup(resp.content, 'lxml')
        cityList = [str(i['value']).strip() for i in soup.find('select', {'id':'NearestFinAdvisorsCity'}).find_all('option') if len(str(i['value']).strip()) > 2]
        print(len(cityList))
        self.cityList = cityList

    
    def getCityData(self, city):
        try:
            data = {
                'nfaType': 'All',
                'nfaARN': '',
                'nfaARNName': '',
                'nfaAddress': '',
                'nfaCity': city,
                'nfaPin': '',
            }

            response = requests.post('https://www.amfiindia.com/modules/NearestFinancialAdvisorsDetails', data=data)
            soup = BeautifulSoup(response.content, 'lxml')
            table = pd.read_html(soup.prettify())[0].drop(['Sr No'], axis=1)
            table = table.where(pd.notnull(table), None)
            self.output.extend(table.to_dict('records'))
            print('Scraped : ', city)
        except Exception as e:
            print(e, '  :  ', city)
            self.getCityData(city)


    def writeXl(self):
        df = pd.DataFrame.from_dict(self.output)
        df.to_excel('output.xlsx')

    def main(self):
        self.getCityList()

        with ThreadPoolExecutor(max_workers=10) as executor:
            executor.map(self.getCityData, self.cityList)

        # for city in self.cityList:
        #     print(city)
        #     self.getCityData(city)

        self.writeXl()


if __name__ == '__main__':
    obj = amfiIndia()
    obj.main()