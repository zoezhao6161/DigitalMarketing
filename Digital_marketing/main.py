import requests
from bs4 import BeautifulSoup
httpscrap = requests.get('https://www.lagreewest.com/')
soup = BeautifulSoup(httpscrap.text,'html.parser')
#Example of Meta description tag code: <meta name="description" content="This is a meta description.
# This text will show up in Google's search engine results page.">
meta_list=soup.find_all('meta')
for meta in meta_list:
    print(meta)