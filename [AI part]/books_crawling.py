from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("C:\\Users\\clstm_\\OneDrive\\Desktop\\New Order\\chromedriver")
driver.implicitly_wait(3)
driver.get('https://blog.aladin.co.kr/town/contents/commentreview?branchtype=1')

#스크롤내리기
for j in range(600):
    driver.find_element_by_css_selector('body').send_keys(Keys.PAGE_DOWN)

#제목과 리뷰데이터 추출
titles = []
reviews = []
for i in range(1, 100):
    for k in range(1, 11):
        title = driver.find_element_by_xpath('/html/body/form/div[4]/div[2]/div/div[3]/table[2]/tbody/tr/td/div[2]/div['+str(i)+']/table['+str(k)+']/tbody/tr/td[3]/table/tbody/tr[1]/td[1]/span[3]').text
        review = driver.find_element_by_xpath('/html/body/form/div[4]/div[2]/div/div[3]/table[2]/tbody/tr/td/div[2]/div['+str(i)+']/table['+str(k)+']/tbody/tr/td[3]/table/tbody/tr[2]/td/div').text
        title = title[1:-1]
        titles.append(title)
        reviews.append(review)

df = pd.DataFrame()
df['title'] = titles
df['review'] = reviews

#별도 csv파일로 저장
df.to_csv('\\book_reviews.csv')