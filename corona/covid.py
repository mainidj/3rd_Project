import requests
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


#코로나 신규 확진자, 누적 확진자 크롤링 ======================
def covid_19() :
    
    Url = "http://www.provin.gangwon.kr/covid-19.html"
    agent_head = {
    "user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36",
    "accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
    }
    
    response = requests.get(Url,headers=agent_head)
    soup = BeautifulSoup(response.text, "html.parser")
    
    a = soup.select('div.condition>ul>li>span') 
    new_covid = a[0].get_text()
    add_covid = a[1].get_text()
    print("신규 확진자 :", new_covid)
    print("누적 확진자 :", add_covid)
    #print(type(new_covid))
    #print(type(add_covid))
#==========================================================

#이벤트 텍스트 크롤링=======================================
def event_text(month) :
   
    eUrl = "https://www.gangwon.to/gwtour/gangwondo_trip/festival_performance?sMonth=" + month
    agent_head = {
    "user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36",
    "accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
    }
    
    response = requests.get(eUrl,headers=agent_head)
    soup = BeautifulSoup(response.text, "html.parser")
    
    #이미지
    image = soup.select('ul.festival_list>li>div.imgs>a')
    for idx in image :
        print(idx["href"])
        
    #링크
    link = soup.select('ul.festival_list>li>div.btn_box>a[href]')
    for idx in link :
        print(idx["href"])
        
    #제목
    title = soup.select('ul.festival_list>li>div.text>strong>a')    


    #장소,기간
    place = soup.find_all('dd')

    temp = []
    for idx in range(int(len(place)/2)):
        curr = []
        sam = place[idx*2].get_text()
        sam = sam.replace("\r\n\t\t\t\t\t\t\t\t\t\t","")
        r = sam.split(" ")
        curr.append(r[0]+r[1])
        test = place[idx*2+1].get_text()
        curr.append(test)
        temp.append(curr)
    
    """
    period_place = soup.select('ul.festival_list>li>div.text>dl>dd')
    period = period_place[0].get_text()
    place = period_place[1].get_text()
    print(b[0].get_text())
    
    
    for no in range(len(title)):
        print("축제명:",title[no].get_text())
        print("모른다:",period[no].get_text())
        print("기간:", period_place[0].get_text())
        #print("장소:", period_place[1].get_text())
        print("==================" * 5)
    """
#==========================================================

def pageNO(month):
    
    eUrl = "https://www.gangwon.to/gwtour/gangwondo_trip/festival_performance?sMonth=" + month
    agent_head = {
    "user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36",
    "accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
    }
    
    response = requests.get(eUrl,headers=agent_head)
    soup = BeautifulSoup(response.text, "html.parser")
    
    
"""
#이벤트 이미지 크롤링=======================================
def event_img(month):
    
    driver = webdriver.Chrome("D:\chromedriver.exe")

    driver.get("https://www.gangwon.to/gwtour/gangwondo_trip/festival_performance?sMonth="+month)
    driver.implicitly_wait(10)
    
    img = driver.find_elements('ul.festval_list>div>a>img')
    img_url = []
    
    for i in img :
        if i.get_attribute('src')!= None :
            img_url.append(i.get_attribute('src'))
        else :
            img_url.append(i.get_attribute('data-src'))
    
    driver.close()
"""
    
    
    
    
month = "05" #월

#covid_19()
event_text(month)
#event_img(month)