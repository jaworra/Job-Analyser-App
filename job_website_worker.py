#Web scapper worker on desktop
#Todo: update for lambda or docker enviroment

from selenium import webdriver
import requests
import webscrapping_worker as webscape


def scaper_via_webdrivers(html_page):
    """ Method callling website uses selenium - webdrivers
    
    Arguments:
        html_page {string} -- Name of webpage
    
    Returns:
        string -- Summarying information on website
    """

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
    """ Method callling website with requests
    
    Arguments:
        html_page {string} -- Name of webpage
    
    Returns:
        string -- Summarying information on website
    """

    #https://codeburst.io/web-scraping-101-with-python-beautiful-soup-bb617be1f486

    try:
        page_response = requests.get(html_page, timeout=5)
    except:
        print("error - with calling website")
        return #for list pass try next key

    try:
        webscape.seek_isolate_contents(page_response,'seek')
    except:
        print("error - isolating key values in website")
        return #for list pass try next key

#scrape from the following websites
page_link1 = 'https://www.seek.com.au/statistician-jobs'
page_link2 = 'https://www.seek.com.au/mathematicians-jobs'

#scaper_via_webdrivers depricated in favour of scaper_via_webdrivers due to transition to lambda code base libraries
#scaper_via_webdrivers(page_link1) 
scaper_via_requests(page_link1)

