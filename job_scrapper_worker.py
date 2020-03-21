#Web scapper worker on desktop
#Todo: update for lambda or docker enviroment

from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import requests

def scaper_via_webdrivers(html_page):
    '''
    method uses selenium - webdrivers
    requires webpage
    '''
    #https://www.edureka.co/blog/web-scraping-with-python/

    #place chrome driver in folder and added to path
    driver = webdriver.Chrome(executable_path=r'C:\webdrivers\chromedriver.exe') #edit this to just look in path variable
    driver.get(page_link1)
    print("Page Title is : %s" %driver.title)
    driver.quit()

    products=[] #List to store name of the product
    prices=[] #List to store price of the product
    ratings=[] #List to store rating of the product
    #driver.get("<a href="https://www.flipkart.com/laptops/">https://www.flipkart.com/laptops/</a>~buyback-guarantee-on-laptops-/pr?sid=6bo%2Cb5g&uniq")
    return

def scaper_via_requests(html_page):    
    '''
    method with requests
    requires webpage
    '''
    #https://codeburst.io/web-scraping-101-with-python-beautiful-soup-bb617be1f486

    page_response = requests.get(html_page, timeout=5)
    page_content = BeautifulSoup(page_response.content, "html.parser")

    print(page_content)

    textContent = []
    for i in range(0, 20):
        paragraphs = page_content.find_all("p")[i].text
        textContent.append(paragraphs)  
    return


#scrape from the following websites
page_link1 = 'https://www.seek.com.au/statistician-jobs'
page_link2 = 'https://www.seek.com.au/mathematicians-jobs'

#scaper_via_webdrivers(page_link1)
scaper_via_requests(page_link1)


