#Python programm to download files from given urls
from selenium import webdriver
driver=webdriver.Chrome(path of driver)
links=["Define links here"]
for link in links:
    print(link)
    print('Downloaded Link:',link)
    driver.get(link)




