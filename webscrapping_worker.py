#isolating contents from different webpages
from bs4 import BeautifulSoup
import pandas as pd
import json

def seek_isolate_contents (page_response, company):
    """Looks at Seek page to isolate relevant material
    
    Arguments:
        page_response {string} -- Contents of webpage
        company {string} -- Name of company
    """
   
    #https://towardsdatascience.com/introduction-to-web-scraping-with-beautifulsoup-e87a06c2b857
    
    print(company)
    page_content = BeautifulSoup(page_response.content, "html.parser")

    #just body extract with charcters
    print(page_content.body.div.div.div.text.strip()) #Statistician Jobs in All Australia
    
    for hit in page_content.findAll(attrs={'class' : '_2iNL7wI'}):
        job_title = hit.text.strip()
        job_type = hit.find_next("p").text.strip().replace("This is a ","").replace("job","").rstrip()
        print(job_title + " (" + job_type + ")") #returns all jobs   


    #remove this below code...
    for hit2 in page_content.findAll(attrs={'class' : ['Eadjc1o','_2iNL7wI']}):
        job_descrip = hit2.text.strip() 
        print(job_descrip)     


    '''
    body = page_content.find('body')
    for job_title in page_content.findAll(attrs={'class' : '_2iNL7wI'}):
        print(job_title) #returns all jobs  
        #tag = job_title.find_next("p")
        #print(tag)
        #for job_descrip in job_title.findAll(attrs={'class' : 'Eadjc1o'}):
        #    print(job_descrip) #returns all job
        #hit = hit.text.strip()
         
    '''
    #print(page_content.body.div.div.text.strip()) 
    body_section = page_content.body.div.div
    #print(page_content.body.div.div) 
    #mydivs = page_content.findAll("body", class_= "_2iNL7wI")
    #print(mydivs)
    #soup = BeautifulSoup(html_page)
    #print(page_content.find('div data-search-sol-meta='))
    #print(page_content.find("body", id="aria-label"))
    #extract body from seek html
    #body = page_content.find('body')
    #print(body)
    #print(soup.find("body", class_="col-l-4 mtop pagination-number")["aria-label"] )
    return

    textContent = []
    job_titles = []
    for i in range(0, 20):
        paragraphs = page_content.find_all("p")[i].text
        textContent.append(paragraphs) 


    return

    '''
    #Future implemenation
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
    '''