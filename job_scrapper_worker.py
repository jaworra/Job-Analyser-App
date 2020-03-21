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

    jobs=[] #List to job titles name
    salaries=[] #List of job salaries  
    ratings=[] #List to job rating
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


#loop through a list of job sites
dataList = [{'seek_stat': 'https://www.seek.com.au/statistician-jobs'},
            {'seek_math': 'https://www.seek.com.au/mathematicians-jobs'},
            {'indeed_stat': 'https://au.indeed.com/jobs?q=statistician&l='},
            {'indeed_math': 'https://au.indeed.com/jobs?q=mathematician&l='},
            {'jora_stat': 'https://au.jora.com/j?q=Statistician&l=Australia&button=&sp=search'}, # format -- https://au.jora.com/cms/get-your-feed-included-on-jora
            {'jora_math': 'https://au.jora.com/j?q=Mathematician&l=Australia&button=&sp=search#email_alert_modal'},
            {'linkedIn_math': 'https://www.linkedin.com/jobs/search/?geoId=101452733&keywords=statistician&location=Australia'},
            {'linkedIn_math': 'https://www.linkedin.com/jobs/search/?keywords=mathematician'},
            #{'monster_math': ''}, #not provided in australia
            ]
for index in range(len(dataList)):
    for key in dataList[index]:
        print(dataList[index][key])

#scrape from the following websites
page_link1 = 'https://www.seek.com.au/statistician-jobs'
page_link2 = 'https://www.seek.com.au/mathematicians-jobs'

#scaper_via_webdrivers depricated in favour of scaper_via_webdrivers due to transition to lambda code base libraries
#scaper_via_webdrivers(page_link1) 
scaper_via_requests(page_link1)

