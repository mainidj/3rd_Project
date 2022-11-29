import requests
from bs4 import BeautifulSoup
import pandas as pd
#from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
import time
import csv


#관광명소 이름, 장소, 이미지 크롤링 ======================

def attraction():
    
    pageS = 59990
    pageE = 60125
    
    agent_head = {
    "user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36",
    "accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
    }
    
    allData = []
    
    for no in range(pageS, pageE+1):
        print("%d / %d 수집.." % (no,pageE))
        Url = "https://www.gangwon.to/gwtour/gangwondo_trip/larvateTravel?articleSeq=" + str(no)
        #print(Url)
        
        response = requests.get(Url,headers=agent_head)
        #print(response)
        soup = BeautifulSoup(response.text, "html.parser")
        #print(response.text)
        list = soup.select('section.container')
        #print(list)
        for item in list:
            
            #제목
            title = item.select_one("header.headerStyle1>h1")
            if title == None :
                print(no, "누락됨....")
                continue
            data_title = title.get_text()

            #장소
            place = item.select('section>div>dl>dd')
            place_data = place[0].get_text()
            
            #이미지
            image = item.select_one("section.imgs>ul>li")
            image_link = image.img["src"]

            data = {"title" : data_title, "price" : place_data, "image" : image_link}
            allData.append(data)
    return allData
    
data = attraction()
print(data)
print("=====" * 30)
df = pd.DataFrame(data)

print(type(df))
print(df)

#df.to_csv('attraction.csv',index=False, encoding='euc-kr')