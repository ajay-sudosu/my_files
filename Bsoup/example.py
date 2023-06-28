from bs4 import BeautifulSoup

soup = BeautifulSoup('<b class="boldest" src="hsd.com" id="tag_test">Extremely bold</b>', features='lxml')
tag = soup.b

# print(tag.text)
# print(tag['class'])

# tag["id"] = "hello TAG"

print(type(tag.attrs))
print(tag.attrs.get("class"))

