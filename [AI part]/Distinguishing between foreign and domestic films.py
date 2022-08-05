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
countrys=[]
for i in range(0,9990):
    # Webdriver에서 네이버 페이지 접속
    driver.get('https://www.naver.com/')
    time.sleep(0.1)
    search_box = driver.find_element(By.NAME, "query")
    search_box.send_keys("영화 "+df["titles"][i] + " 정보")
    search_box.send_keys(Keys.RETURN)
    time.sleep(0.1)
    path = "#main_pack > div.sc_new.cs_common_module.case_empasis.color_14._au_movie_content_wrap > div.cm_content_wrap > div.cm_content_area._cm_content_area_info > div > div.detail_info > dl"
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    for j in soup.find_all("div",{"class":"info_group"}):
        country = j.get_text()
        print(country)
        countrys.append(country)
    if(i%1000==0):
        print(i)

#부분 run: alt+shift+E
#따로 인덱스에 저장
df['info'] = countrys
df.to_csv('movie_reviews_ver3.csv')


isit_domestic = []
for i in range(0,9990):
    if countrys[i].find("국가") != -1:  #find()는 문자열에 인자로 전달된 문자열이 존재할 때, 문자열의 위치에 해당하는 index를 리턴합니다.문자열이 존재하지 않으면 -1을 리턴합니다. find가 -1을 리턴하지 않으면 문자열이 포함되어있다고 판단할 수 있습니다
        if countrys[i].find("한국") != -1:
            isit_domestic[i] = True
            print(isit_domestic[i])
        else:
            isit_domestic[i] = False
            print(isit_domestic[i])
    else:
        isit_domestic[i] = "ERROR"
        print(isit_domestic[i])

df.to_csv('movie_reviews_ver3.csv')