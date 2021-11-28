# Web Scraping tutorial for http:quotes.toscrape.com where we are going to scrape data for Quotes, Authors and Tags 

from bs4 import BeautifulSoup
import requests
import lxml

url = 'http://quotes.toscrape.com'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
quotes = soup.find_all('span', class_='text')
authors = soup.find_all('small', class_='author')
tags = soup.find_all('div', class_='tags')
for i in range(0, len(quotes)):
  print(quotes[i].text)
  print(authors[i].text)
  quoteTags = tags[i].find_all('a', class_='tag')
  for quoteTag in quoteTags:
    print(quoteTag.text)

#End of Tutorial Simple Web Scraping 
