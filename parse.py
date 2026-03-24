# pip install requests
# pip install beautifulsoup4

# Python Parse URL and Data Scraping
import requests
from bs4 import BeautifulSoup

data = requests.get('https://www.azadchaiwala.com/')
print(data.content)

soup = BeautifulSoup(data.content, features="html.parser")

print(soup.html.head.title)

print(soup.find_all('a'))

for a in soup.find_all('a'):
    print(a)

for d in soup.find_all("div" , class_="course-title"):
    print(d)
