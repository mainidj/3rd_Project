import requests
from bs4 import BeautifulSoup
import pandas as pd
#from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
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
    #print(type(add_covid))p
    return new_covid, add_covid
#==========================================================

#이벤트 텍스트 크롤링=======================================
def event_text(month) :
   
    pageS = 1
    pageE = 100
    
    agent_head = {
    "user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36",
    "accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
    }
    
    allData = []
    
    for no in range(pageS, pageE+1) :
        #print("%d / %d 페이지 수집중...." % (no,pageE))
        Url = "https://www.gangwon.to/gwtour/gangwondo_trip/festival_performance?mode=&pageIndex="+ str(no) +"&sMonth="+month    
        
        response = requests.get(Url,headers=agent_head)
        soup = BeautifulSoup(response.text, "html.parser")        
        
        #목록 얻기
        list = soup.select('ul.festival_list > li')
        
        for item in list :
            
            #제목
            title = item.select_one("div.text > strong > a")
            if title == None :
                #print("마지막 페이지 입니다.");
                return allData
            data_title = title.get_text()
            
            #이미지
            image = item.select_one("div.imgs > a")
            data_link  = image["href"]
            image_link = image.img["src"]
            
            #기간,장소
            place = item.select('dd')

            data_time = place[0].get_text()
            data_time = data_time.replace("\t","")
            data_time = data_time.replace("\r","")
            data_time = data_time.replace("\n","") 
            data_time = data_time.replace(" ","")  
            
            data_place = place[1].get_text()
            data_place = data_place.replace("\t","")
            data_place = data_place.replace("\r","")
            data_place = data_place.replace("\n","")
            data_place = data_place.replace(" ","")
            
            """
            print(data_title)
            print(data_link)
            print(image_link)
            print(data_time)
            print(data_place)
            print("=" * 40)
            """
           
            data = { "title" : data_title, "link" : data_link, "image" : image_link , "time" : data_time, "place" : data_place }
            allData.append(data)
    return allData
#==========================================================

    
#covid_19()
event_list = []
month_list = [ "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12" ]
for month in month_list :
    #print(month + "월 수집중.....")
    data = event_text(month)
    for item in data :
        event_list.append(item)
        #print(item)
        #print("=" * 40)

print(event_list)

df = pd.DataFrame(event_list)
print("=" * 40)
print(type(df))
print("=" * 40)
print(df)

df.to_csv('event.csv',index=False, encoding='euc-kr')
"""
new, add= covid_19()
print(type(new))
"""


