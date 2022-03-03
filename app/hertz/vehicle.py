
import requests



def test():
    _BASE_URI = 'https://www.autotrader.co.uk'
    url = f'{_BASE_URI}/json/search/options?advertising-location=at_cars'
    resp = requests.get(url)
    resp.raise_for_status()
    return (r['displayName'] for r in resp.json()['options']['make'])

if __name__ == '__main__':
    test()
