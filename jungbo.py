import requests
from bs4 import BeautifulSoup
import re

url = "https://eomisae.co.kr/index.php?mid=ec&page=1"
res = requests.get(url)
res.raise_for_status
soup = BeautifulSoup(res.text ,"lxml")
values = soup.find_all("a",{"class":"title pjax fw_l"})
urls = []
names = []
count = 20
def make_name():
    for i in range(len(values)):
        
        names.append(values[i].get_text())

    return names

def make_url():
    for i in range(len(values)):

        urls.append(values[i]["href"])
    return urls