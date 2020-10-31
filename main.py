from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

driver = webdriver.Chrome()

problems = []

driver.get("https://cses.fi/problemset/")

content  = driver.page_source

#print(content)

soap = BeautifulSoup(content)

for li in soap.findAll('li' ,attrs = {'class' : 'task' } ):
    for a in li.findAll('a' , href = True  ):
        print( a['href'] , a.text)