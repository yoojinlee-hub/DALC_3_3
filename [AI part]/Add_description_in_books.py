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

df = pd.read_csv("book_reviews.csv")

# Webdriver 실행
driver = webdriver.Chrome('D:/chromedriver.exe')

path='//*[@id="kp-wp-tab-overview"]/div[2]/div/div/div/div/div/div[2]/div/div/div/span[1]'

#자동 검색 + 정보 저장
descriptions = []
for i in range(0,3770):
    #초기화
    description = []
    sentences = []
    # Webdriver에서 네이버 페이지 접속
    driver.get('https://www.naver.com/')
    time.sleep(0.1)
    search_box = driver.find_element(By.NAME, "query")
    if(type(df["title"][i])==str):
        search_box.send_keys(df["title"][i] + " 책소개")
        search_box.send_keys(Keys.RETURN)
        time.sleep(0.1)
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        for j in soup.find_all("p", {"class": "publisher_box"}):
            sentence = j.get_text()
            sentences.append(sentence)
        description = ''.join(sentences)
        descriptions.append(description)
        print(i)
        print(descriptions[i])
    else:
        description=''
        descriptions.append(description)

#따로 인덱스에 저장
df['descriptions']=descriptions
df.to_csv('book_reviews_with_descriptions.csv')