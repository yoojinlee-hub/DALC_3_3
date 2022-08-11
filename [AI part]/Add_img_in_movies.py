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

df = pd.read_csv("movie_reviews_with_komoran.csv")

# Webdriver 실행
driver = webdriver.Chrome('D:/chromedriver.exe')

#자동 검색 + 정보 저장
imgs = []
for i in range(0,9990):
    # 초기화
    img_url = []
    A = []
    # Webdriver에서 네이버 페이지 접속
    driver.get('https://www.naver.com/')
    time.sleep(0.1)
    search_box = driver.find_element(By.NAME, "query")
    search_box.send_keys("영화 "+df["titles"][i])
    search_box.send_keys(Keys.RETURN)
    time.sleep(0.1)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    soup1 = soup.find("a", {"class": "thumb _item"})
    if soup1 != None:
        A = str(soup1).split(" src=")
        img_url = A[1].split("width=")[0]
        img = img_url.replace('"', '')
    else:
        img = "ERROR"
    imgs.append(img)
    print(i)
    print(img)

#따로 인덱스에 저장
df['imgs_url']=imgs
df.to_csv('movie_reviews_with_komoran.csv')
