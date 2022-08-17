import numpy as np
import nltk
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

#nltk.download() #https://www.nltk.org/data.html
file_path = "to_clean.txt"
nltk.download('punkt')

with open(file_path) as f:
    lines = f.readlines()
lines = [line.rstrip('\n') for line in lines]
stop_words=['이', '있', '하', '것', '들', '그', '되', '수', '이', '보', '않', '없', '나', '사람', '주', '아니', '등', '같', '우리', '때', '년', '가', '한', '지', '대하', '오', '말', '일', '그렇', '위하','있다','하다']
stop_words= lines + stop_words

df = pd.read_csv("book_reviews_with_komoran.csv")
x_data = df['komoran']

clean_words = []
for k in range(0,3):
    for document in x_data[k]:
        clean_word = []
        cleaned = 0
        for word in document:
            if word not in stop_words:  # 불용어 제거
                clean_word.append(word)
    print(k)
    print(cleaned)
    print(x_data[k])
    print(clean_word)
    clean_words.append(clean_word)


#따로 인덱스에 저장
df['cleaned_token']=clean_words
df.to_csv('book_reviews(cleaned).csv')
