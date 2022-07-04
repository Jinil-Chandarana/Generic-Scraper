from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
from lxml import etree
from bs4 import BeautifulSoup
import lxml.html
from joblib import Parallel, delayed
import threading

Dict_Headers = ({'User-Agent':
                     'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 \
      (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36', \
                 'Accept-Language': 'en-US, en;q=0.5'})
url = "https://www.carlinoguitars.com/austin-guitars"
driver = webdriver.Chrome("C:\\chromedriver_win32\\chromedriver.exe")
driver.get(url)
driver.implicitly_wait(10)
webPage = requests.get(url, Dict_Headers)
Scraping = BeautifulSoup(webPage.content, "html.parser")
documentObjectModel = etree.HTML(str(Scraping))
tags = documentObjectModel.xpath("//*")
#
# ipath = "//*[@class='comp-ka2mgepx']//img"
# img = driver.find_elements(By.XPATH, ipath)
# print(len(img))

# sum = 0
classset = set()
for tag in tags:
    div = etree.tostring(tag).decode('utf-8')
    el = lxml.html.fromstring(div)
    cls = el.get('class')

    cpath = "//*[@class='" + str(cls) + "']"
    class_ = documentObjectModel.xpath(cpath)

    if ((len(class_) >= 2)):
        classset.add(el.get('class'))
print(len(classset), classset)

ssum = 0
final = set()
for ele in classset:
    ssum += 1
    print(ssum)
    ipath = "//*[@class='" + str(ele) + "']//img"
    img = (driver.find_elements(By.XPATH, ipath))
    if ((len(img)) >= 2):
        final.add(ele)

# def img_filter(ele):
#     final = set()
#     ipath = "//*[@class='" + str(ele) + "']//img"
#     img = (driver.find_elements(By.XPATH, ipath))
#     if ((len(img)) >= 2):
#         final.add(ele)
#     return final
#
# for ele in classset:
#     t = threading.Thread(target=img_filter, args=(ele))
#     t.start()
#     threads.append(t)
#
# for thread in threads:
#     thread.join()
# # final.add(Parallel(n_jobs=-1)(delayed(img_filter)(ele) for ele in classset))

print(final)

