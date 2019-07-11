from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
url="http://techo2.com/"
page=urlopen(url)
page_information=soup(page,'html.parser')
text=page_information.text
with open("Techo2.txt",'w') as file:
    file.write(text)