# -*- coding: utf-8 -*-
"""

@author: Louw Redelinghuys
"""

# GOAL :    Get title of every book with a 2 star rating

import requests
import bs4

#Remember to: pip install beautifulsoup4

base_url = 'http://books.toscrape.com/catalogue/page-{}.html'

res = requests.get(base_url.format(1))
soup = bs4.BeautifulSoup(res.text,'lxml')

products = soup.select('.product_pod')

example = products[0]


#print(example)

#quick and dirty:
if 'star-rating Three' in str(example):
    pass
    
# using Beautiful soup   
if example.select(".star-rating.Three") == []:  #need to use . in place of spaces
    pass

exampletitle = example.select('a')[1]['title']


#putting it all together

two_star_titles = []

for n in range(1,51):
    scrape_url = base_url.format(n)
    res = requests.get(scrape_url)
    
    soup = bs4.BeautifulSoup(res.text,'lxml')
    books = soup.select(".product_pod")
    
    for book in books:
        if len(book.select('.star-rating.Two')) != 0:
            book_title = book.select('a')[1]['title']
            two_star_titles.append(book_title)
            
            
print(two_star_titles[0])






 
