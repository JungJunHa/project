from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests
from bs4 import BeautifulSoup
import pandas as pd
import urllib.request
import time

word_list = ['baby fall','baby fallen','baby fall down','baby fell down']

driver = webdriver.Chrome("C:/Users/JJH/Desktop/chromedriver_win32/chromedriver.exe")
driver.get('https://www.youtube.com')
time.sleep(3)
video_title = []
video_link = []
for word in word_list:
    search = driver.find_element_by_id("search")
    search.clear()
    search.send_keys(word)
    search.send_keys(Keys.RETURN)
    time.sleep(5)

    for _ in range(3):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(5)

    html = driver.page_source
    soup = BeautifulSoup(html)
    
    titles = soup.find_all('a', {'id' : 'video-title'})
    links = soup.find_all('a', {'id' : 'video-title'})
    for i in range(len(soup.find_all('ytd-video-meta-block', 'style-scope ytd-video-renderer byline-separated'))):
        video_title.append(titles[i].text.replace('\n', ''))
        video_link.append('https://www.youtube.com/' + links[i]['href'])

video_list = pd.DataFrame(columns=['title', 'link'])
video_list['title'] = video_title
video_list['link'] = video_link
video_list.to_csv('C:/Users/JJH/Desktop/baby_fall.csv', index=False)

driver.close()
