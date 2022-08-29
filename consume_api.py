import requests
from bs4 import BeautifulSoup

IMDB_ID = 'tt9916730'


def get_imdb_extra_data(imdb_id):
    response = requests.get(f'https://www.imdb.com/title/{imdb_id}/')
    bs = BeautifulSoup(response.text, 'html.parser')
    return bs.find('span', {'data-testid': "plot-xl"}).text


if __name__ == '__main__':
    get_imdb_extra_data(IMDB_ID)