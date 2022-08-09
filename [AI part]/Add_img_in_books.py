import selenium as selenium
import pandas as pd
import numpy as np
import re
import matplotlib.pyplot as plt
from selenium.webdriver.common.keys import Keys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

df = pd.read_csv("book_reviews_with_descriptions.csv")

# Webdriver 실행
driver = webdriver.Chrome('D:/chromedriver.exe')

#자동 검색 + 정보 저장
imgs = []
#자동 검색 + 정보 저장
imgs = []
for i in range(0,3770):
    # 초기화
    img_url = []
    A = []
    # Webdriver에서 네이버 페이지 접속
    driver.get('https://www.naver.com/')
    time.sleep(0.1)
    search_box = driver.find_element(By.NAME, "query")
    if (type(df["title"][i]) == str):
        search_box.send_keys("책 "+df["title"][i])
        search_box.send_keys(Keys.RETURN)
        time.sleep(0.1)
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        soup1 = soup.find("img", {"class": "thumb api_get"})
        if soup1 != None:
            A = str(soup1).split(" src=")
            img_url = A[1].split("width=")[0]
            img = img_url.replace('"', '')
        else:
            img = "ERROR"
        imgs.append(img)
    else:
        img = "ERROR"
        imgs.append(img)
    print(i)
    print(img)


#따로 인덱스에 저장
df['imgs_url']=imgs
df.to_csv('book_reviews(descriptions,img_url).csv')
