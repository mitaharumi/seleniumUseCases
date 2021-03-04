'''
---------------------------------
--------- fence caption ---------
---------------------------------
- # code and others explanation -
- ## thoughts                   -
- ### suggestion                -
- #### fix later                -
- ##### bug                     -
---------------------------------
'''

from access import pathChromeDriver
from selenium import webdriver
import time as t

driver = webdriver.Chrome(pathChromeDriver())
url = 'https://pypi.org/search/?q=selenium'
driver.get(url)

id = 0
# take 3 first pages
page = 0
while page < 3:
    t.sleep(5)
    content = driver.find_element_by_xpath('//*[@id="content"]/div/div/div[2]/form/div[3]')
    with open (f'{str(id)}.csv', 'w', encoding='UTF-8') as csv:
        csv.write(content.text)

    t.sleep(1)

    #### gambiarra
    # button next a[index] is dynamic

    index = 7
    try:
        print(f'//*[@id="content"]/div/div/div[2]/form/div[3]/div/a[{str(index)}]')
        nextPage = driver.find_element_by_xpath(f'//*[@id="content"]/div/div/div[2]/form/div[3]/div/a[{str(index)}]')
        nextPage.click()
    except:
        try:
            print(f'//*[@id="content"]/div/div/div[2]/form/div[3]/div/a[{str(index-1)}]')
            nextPage = driver.find_element_by_xpath(f'//*[@id="content"]/div/div/div[2]/form/div[3]/div/a[{str(index-1)}]')
            nextPage.click()
        except:
            print(f'//*[@id="content"]/div/div/div[2]/form/div[3]/div/a[{str(index-2)}]')
            nextPage = driver.find_element_by_xpath(f'//*[@id="content"]/div/div/div[2]/form/div[3]/div/a[{str(index-2)}]')
            nextPage.click()
    page = page + 1
    id = id + 1
