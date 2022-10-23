
from bs4 import BeautifulSoup


import requests


def scraping():
    URL_SCRAPING = 'https://usa.avtopmr.com/catalog/'
    resp = requests.get(URL_SCRAPING, timeout=10.0)
    if resp.status_code != 200:
        raise Exception('HTTP error access!')

    data_list = []
    html = resp.text
    soup = BeautifulSoup(html, 'html.parser')
    blocks = soup.select("title")
    for block in blocks:
        print(f'HTML text consists of {len(block.text)} symbols')
        print(50 * '=')
        print(block.text)
        break



if __name__ == '__main__':
    scraping()
