#pip install requests
#pip install beautifulsoup4

import requests
from bs4 import BeautifulSoup

url = 'https://example.com'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
print(soup.prettify())

#find by tag, returns first title
title = soup.title
print(title)

#get just the text
title = soup.title.string
print(title)

#find by tags that aren't just the first in a document
url = 'https://www.wm.edu/as/computerscience/people/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
print(soup.prettify())

paragraphs = soup.find_all("p")
print(paragraphs)
print(paragraphs[0])

#locating text from a string
office = soup.find_all(string="Faculty")
print(office) #not helpful at all
print(office[0].parent)
print(office[0].parent.string)

#locating using classes
professors = soup.find_all("article", class_="item_listing directory_listing")
print(professors[0])
print(professors[0].find("p"))
print(professors[0].find("p").find("a"))
print(professors[0].find("p").find("a").string)

for i in range(len(professors)):
    print(professors[i].find("p").find("a").string)







