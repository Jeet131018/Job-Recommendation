from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

from bs4 import BeautifulSoup
from time import sleep
from skill_list import skills
import os

import pandas as pd



driver_path = "./chromedriver.exe"
service = Service(executable_path=driver_path)
options = webdriver.ChromeOptions()
web = webdriver.Chrome(service=service,options=options)

def do():
    ex = []
    wrong = []
    
    # db = client['jobs'] 
    # db.create_collection('narkuri') 
    # print("Database created........") 
    final_data=[]
    t = 0
    # url = "https://www.naukri.com/Cryptography-jobs?k=Cryptography"
    # print(url)
    # web.get(url)
    
    # html = web.page_source
    for search in skills:
        try:
            print("index:" ,t)
            t+=1
            search_title = search
            url = "https://www.naukri.com/" + search_title + "-jobs?k=" + search_title
            print(url)
            web.get(url)

            sleep(1)
            html = web.page_source
            soup = BeautifulSoup(html)

            data = []

            TITLE         = soup.find_all("a", {"class": "title"})
            EXPERIENCE    = soup.find_all("li", {"class": "experience"}) 
            SALARY        = soup.find_all("li", {"class": "salary"})
            LOCATION      = soup.find_all("li", {"class": "location"})
            SKILLS        = soup.find_all("ul", {"class": "has-description"})   

            for i in range(20):
                
                x = {
                    'title'     : TITLE[i].text,
                    'url'       : TITLE[i].get('href'),
                    'experience': EXPERIENCE[i].text,
                    'salary'    : SALARY[i].text,
                    'location'  : (LOCATION[i].text).split(', '),
                    'skills'    : [j.text for j in SKILLS[i]],
                    'search_type'      : search_title
                }

                data.append(x)
            
            
            final_data.append(data)
            # print(data)
            # db = client['jobs'] 
            # mydb = db['narkuri']

            # x = mydb.insert_many(data)

        except Exception as e:
            ex.append(e)
            wrong.append((search , url))
    
    # print(final_data)
    columns = ['title','url','experience','salary','location','skills','search_type']
    df = pd.DataFrame(final_data,columns=columns)
    df.to_csv("MyDataset1")
    

do()