#Python programm to download files from given urls
from selenium import webdriver
driver=webdriver.Chrome('/home/ganapathi/Downloads/chromedriver')
links=[
    'https://login.globaldata.com/Login/IPLogin?ReferrerIC=ph&ReturnUrl=/Reports/ExportFullReportToWord/Respiratory-Syncytial-Virus--Epidemiology-Forecast-in-Asia-Pacific-Markets-to-2028',
    'https://login.globaldata.com/Login/IPLogin?ReferrerIC=ph&ReturnUrl=/Reports/ExportFullReportToWord/Female-Infertility--Opportunity-Analysis-and-Forecasts-to-2028',
    'https://login.globaldata.com/Login/IPLogin?ReferrerIC=ph&ReturnUrl=/Reports/ExportFullReportToWord/Myasthenia-Gravis--Epidemiology-Forecast-to-2028',
    'https://login.globaldata.com/Login/IPLogin?ReferrerIC=ph&ReturnUrl=/Reports/ExportFullReportToWord/Ovarian-Cancer--Opportunity-Analysis-and-Forecasts-to-2028',
    'https://login.globaldata.com/Login/IPLogin?ReferrerIC=ph&ReturnUrl=/Reports/ExportFullReportToWord/Gene-Therapy-in-Neurology'
]
for link in links:
    print(link)
    print('Downloaded Link:',link)
    driver.get(link)




