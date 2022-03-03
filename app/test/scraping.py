from requests import get
from bs4 import BeautifulSoup


url = 'https://www.hertz.com/rentacar/location#cities'
response = get(url)
html_soup = BeautifulSoup(response.text, 'html.parser')
print (html_soup)