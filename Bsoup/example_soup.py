from bs4 import BeautifulSoup
import requests

url = 'https://vahan.parivahan.gov.in/vahan4dashboard/vahan/view/reportview.xhtml'

data = requests.get(url)

soup = BeautifulSoup(data.text, features='xml')

# print(soup.prettify())

# gives the first title tag text
# title = soup.title.text
# print(title)

# Gives the first div and its nested tags and elements.
# div = soup.div
# print(div)


# find
div = soup.find('div', class_='navbar-header')
print('This is an anchor text--', div.a.text)

# To get the attribute of a tag.
article = soup.find('div', class_="you-tube-video")["src"]



