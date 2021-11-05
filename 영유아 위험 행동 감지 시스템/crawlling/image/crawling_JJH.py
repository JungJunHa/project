from selenium import webdriver
import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.parse import quote_plus
from selenium.webdriver.common.keys import Keys
import time
import urllib.request


# words = [['chalk','chalk picture','one chalk','color chalk','white chalk'],['pencil','color pencil','pencils','4b pencil','2b pencil'],
words = [['pen','one pen','color pen','pens','pentel']]

driver = webdriver.Chrome("C:/Users/JJH/Desktop/chromedriver_win32/chromedriver.exe")
driver.get("https://www.google.co.kr/imghp?hl=ko&ogbl")

for word_list in words:
    n = 1
    for word in word_list:
        elem = driver.find_element_by_name("q")
        elem.clear()
        elem.send_keys(word)
        elem.send_keys(Keys.RETURN)
        time.sleep(2)
        for _ in range(3):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(3)
        list_word = driver.find_elements_by_css_selector('.rg_i.Q4LuWd')
        try_numb = 1
        for image in list_word:
            try: 
                image.click()
                time.sleep(3)
                imgUrl = driver.find_element_by_xpath('/html/body/div[2]/c-wiz/div[3]/div[2]/div[3]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div[2]/div[1]/a/img').get_attribute("src")
                # print(imgUrl)
                # urllib.request.urlretrieve(imgUrl, str(n) + ".jpg")
                with urlopen(imgUrl) as f:
                    with open('C:/Users/JJH/Desktop/{}/'.format(word_list[0]) + str(n)+'.jpg','wb') as w:
                        img = f.read()
                        w.write(img)
                n = n + 1
                try_numb += 1
            except:
                pass
            if try_numb>200:
                break
driver.close()
#     response = requests.get(source, headers = headers)
#     soup = BeautifulSoup(response.text, 'html.parser')
#     for _ in soup.find_all('img',attrs = {'class':'Q4LuWd'}):
#         print(_.attrs['src'])
