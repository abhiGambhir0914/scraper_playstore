import requests
from bs4 import BeautifulSoup,SoupStrainer
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# -*- coding: utf-8 -*-
import sys
import codecs
 
# =============================================================================
# if sys.stdout.encoding != 'cp850':
#   sys.stdout = codecs.getwriter('cp850')(sys.stdout.buffer, 'strict')
# if sys.stderr.encoding != 'cp850':
#   sys.stderr = codecs.getwriter('cp850')(sys.stderr.buffer, 'strict')
# =============================================================================
 
url = "https://www.appbrain.com/stats/google-play-rankings/top_free/all/{country}/{page}"
 
 
def selenium_parse(driver,country,page):
    print(f'get:{url}')
   
    driver.get(url.format(country = country, page=page))
    try:
        element = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "page-top-header")))
    except:
        print('ERROR: Explicit wait timout..')
    with open(f'output/page_{country}_{page}.html',mode='w+',encoding="utf-8") as op:
        op.write(driver.page_source)
    # driver.quit()
    print(f'Page saved:{page}')
 
   
if __name__ == "__main__":
    # data = parse(fetch_html())
    driver  = webdriver.Chrome(executable_path="/Users/abhigambhir/Desktop/chromedriver")
    countries = ['in','us','au','at','be','br','ca','cz','dk','fi','fr','de','ir','it','jp','mx','nl','no','pl','pt','ru','sa','sk','kr','es','se','ch','tr','gb']
    for country in countries:
        for page in range(1,6):    
            selenium_parse(driver, country,page)
        print(f'Country[{country}] Done..')
    print('\n\nAll Jobs Done')
    # print(data)