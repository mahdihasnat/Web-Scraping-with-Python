from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import keyboard


def get_problem(driver , url ):

    driver.get(url)
    content = driver.page_source

    soap = BeautifulSoup(content )

    result = {}

    name = soap.findAll('h1')[0] .text

    result['problem_name'] = name


    constraints = soap.findAll('ul' , attrs = {'class' : 'task-constraints'})[0]
    for constraint in constraints.findAll('li' ):
        print(constraint)
        lst = constraint.text.split(' ')
        result[str(lst[0].lower()) + '_limit' ] = lst[-2]
    x = result['time_limit']
    x = float(x) * 1000
    x = int(x)
    result['time_limit'] = x


    return result

def debug():
    content =  open('sample.html' , 'r').read()

    soap = BeautifulSoup(content  , 'lxml')

    result = {}

    name = soap.findAll('h1')[0] .text

    result['problem_name'] = name


    constraints = soap.findAll('ul' , attrs = {'class' : 'task-constraints'})[0]
    for constraint in constraints.findAll('li' ):
        lst = constraint.text.split(' ')
        result[str(lst[0].lower()) + '_limit' ] = lst[-2]
    x = result['time_limit']
    x = float(x) * 1000
    x = int(x)
    result['time_limit'] = x


    problem_content = soap.findAll('div' , attrs = {'class':'content'})[0]
    print(problem_content.text)

    print(result)

def main():

    driver = webdriver.Chrome('chromedriver.exe')

    problems = []



    driver.get("https://cses.fi/login/")

    keyboard.wait('f5')

    driver.get("https://cses.fi/problemset/")

    content  = driver.page_source

    #print(content)

    soap = BeautifulSoup(content)

    for li in soap.findAll('li' ,attrs = {'class' : 'task' } ):
        nibo = False
        if li.findAll('span' , attrs = {'class':'task-score icon full'}) :
            nibo = True
        if nibo :
            for a in li.findAll('a' , href = True  ):
                print( a['href'] , a.text )
                print( get_problem(driver, 'https://cses.fi' + a['href']))


if __name__ == '__main__':
    main()
    debug()

