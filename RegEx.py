from bs4 import BeautifulSoup
from urllib.request import urlopen
import re

html = urlopen("https://morvanzhou.github.io/static/scraping/table.html").read().decode('utf-8')
print(html)
soup = BeautifulSoup(html, features='lxml')
img_links = soup.find_all('img', dict(src=re.compile('.*?\.jpg')))
for link in img_links:
    print(link['src'])
course_links = soup.find_all('a', dict(href=re.compile('https://morvan.*')))
for link in course_links:
    print(link['href'])
