#한글형태소 추출 라이브러리 설치
from konlpy.tag import Komoran
komoran = Komoran()


import pandas as pd
import numpy as np

#영화 리뷰데이터 가져오기
reviews = pd.read_csv('book_reviews(descriptions,img_url)_ansi.csv') # 'utf-8' codec can't decode byte 0xb3 in position 67: invalid start byte
print(reviews.iloc[0, 4])
lists = []

#토큰화 진행
for i in range(0, reviews.shape[0]):
  mini_1 = komoran.pos(reviews.iloc[i, 4]) #java.lang.NullPointerException: java.lang.NullPointerException
  mini_2 = []
  for k in mini_1:
    if k[1] in ('NNG', 'NNP', 'MM', 'MAG', 'IC', 'NF', 'NV'):
      mini_2.append(k[0])
    elif k[1] in ('VV', 'VA'):
      mini_2.append(k[0]+"다")
  lists.append(mini_2)

#리스트에 저장 후 영화리뷰데이터에 별도 열로 추가
reviews['komoran'] = lists
print(reviews)