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

# Webdriver 실행
browser = webdriver.Chrome('D:/chromedriver.exe')

# Webdriver에서 네이버 페이지 접속
browser.get('https://www.naver.com/')
time.sleep(0.3)

countrys=[]
search_box = browser.find_element(By.NAME, "query")
search_box.send_keys(df["titles"][0]+" 정보")
find_site = search_box.send_keys(Keys.RETURN)
explanation = find_site.find_element_by_class_name("_content_text").text
print(country)
