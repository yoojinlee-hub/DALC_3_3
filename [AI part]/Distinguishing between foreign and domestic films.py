import selenium as selenium
import pandas as pd
import numpy as np
import re
import matplotlib.pyplot as plt

df = pd.read_csv("movie_reviews2.csv")
#df["titles"]

from selenium.webdriver.common.keys import Keys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

# Webdriver 실행
driver = webdriver.Chrome('D:/chromedriver.exe')

#자동 검색 + 정보 저장
isit_domestic = []
for i in range(0,9990):
    #초기화
    countrys = []
    sentences = []
    # Webdriver에서 네이버 페이지 접속
    driver.get('https://www.naver.com/')
    time.sleep(0.1)
    search_box = driver.find_element(By.NAME, "query")
    search_box.send_keys("영화 "+df["titles"][i] + " 정보")
    search_box.send_keys(Keys.RETURN)
    time.sleep(0.1)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    for j in soup.find_all("div", {"class": "info_group"}):
        country = j.get_text()
        countrys.append(country)
    sentences =  ''.join(countrys)
    if "국가" in sentences:  # find()는 문자열에 인자로 전달된 문자열이 존재할 때, 문자열의 위치에 해당하는 index를 리턴합니다.문자열이 존재하지 않으면 -1을 리턴합니다. find가 -1을 리턴하지 않으면 문자열이 포함되어있다고 판단할 수 있습니다
        if "한국" in sentences:
            isit_domestic.append(True)
        else:
            isit_domestic.append(False)
    else:
        isit_domestic.append("ERROR")
    print(i)
    print("번째:")
    print(isit_domestic[i])


#따로 인덱스에 저장
df['info'] = countrys
df['country']=isit_domestic
df.to_csv('movie_reviews_ver3.csv')