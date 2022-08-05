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

# Webdriver에서 네이버 페이지 접속
driver.get('https://www.naver.com/')
time.sleep(0.3)

countrys=[]
for i in range(0,9990):
    driver.get('https://www.naver.com/')
    time.sleep(0.2)
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



