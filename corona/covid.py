import requests
from bs4 import BeautifulSoup
import pandas as pd


Url = "http://www.provin.gangwon.kr/covid-19.html"
agent_head = {
"user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36",
"accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
}

response = requests.get(Url,headers=agent_head)
soup = BeautifulSoup(response.text, "html.parser")

a = soup.select('div.condition>ul>li>span') 
print(a)



b = soup.find('div').find('ul').find('li').find('span')
print(b.get_text())


