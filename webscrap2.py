import requests
from bs4 import BeautifulSoup
import re
import urllib.request

url= "https://ful.io"

page = requests.get(url)
page.content
soup = BeautifulSoup(page.content,'html.parser')

para = soup.find_all('a')
all_links = []

for link in para:
    if link.get('href') != '#':
        link = link.get('href')
        all_links.append(link)
        print("social link:",link)


with urllib.request.urlopen(url) as response:
    page_bytes = response.read()
    
the_page = page_bytes.decode('utf-8')

email_patterns = re.compile("[-a-zA-Z0-9._]+@[-a-zA-Z0-9._]+.[-a-zA-Z0-9._]")
emails = re.findall(email_patterns,the_page)
print("Email :", emails)

