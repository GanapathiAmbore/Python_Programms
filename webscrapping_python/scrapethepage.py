from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
url="http://xyz.com/"
page=urlopen(url)
page_information=soup(page,'html.parser')
text=page_information.text
with open("xyz.txt",'w') as file:
    file.write(text)
