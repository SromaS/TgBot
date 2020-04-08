import requests
from bs4 import BeautifulSoup

base_url = 'https://coinmarketcap.com/'
headers = ['|', '| ', '| Market Cap:', '| Price:', '| Volume (24h):', '| Circulating Supply:', '| Change (24h):']


def get_html(url):
    doc = requests.get(url).text
    return doc


def coinMarket_parse(html_page, count):
    soup = BeautifulSoup(html_page)
    table = soup.findAll('tr', {'class': 'cmc-table-row'})
    result = ''
    tr_count = 1
    currencies = []
    for tr in table:
        if tr_count <= count:
            #достали все столбцы в массив
            col=1
            row = tr.findAll('td', {'class': 'cmc-table__cell'})
            currency = []
            for td in row[:7]:
                if col == 1:
                    div = td.find('div', {'class': ''}).text
                    currency.append(div)
                elif col == 2:
                    a = td.find('a').text
                    currency.append(a)
                elif col == 3:
                    div = td.find('div', {'class': ''}).text
                    currency.append(div)
                elif col == 4:
                    a = td.find('a').text
                    currency.append(a)
                elif col == 5:
                    a = td.find('a').text
                    currency.append(a)
                elif col == 6:
                    div = td.find('div', {'class': ''}).text
                    currency.append(div)
                else:
                    if td.find('div', {'class': 'cmc--change-negative'}) is None:
                        prc = td.find('div', {'class': 'cmc--change-positive'}).text
                    else:
                        prc = td.find('div', {'class': 'cmc--change-negative'}).text
                    currency.append(prc)
                col += 1
            currencies.append(currency)
            tr_count += 1
        else:
            break
    for currency in currencies:
        i = 0
        str = ''
        for header in headers:
            str += header+' ' + currency[i]+' '
            i += 1
        result += str+'\n\n'
    return result




