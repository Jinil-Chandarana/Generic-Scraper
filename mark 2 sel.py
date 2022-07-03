from imp import source_from_cache
from turtle import delay
import requests
from lxml import etree
from bs4 import BeautifulSoup
import lxml.html
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium import * 
import time
driver = webdriver.Chrome("C:\\chromedriver_win32\\chromedriver.exe")
driver.get("https://www.flipkart.com/wearable-smart-devices/smart-watches/~cs-5ciwhiz2cg/pr?sid=ajy%2Cbuh&collection-tab-name=Samsung+Watch+4&bu=SHOPSY&ctx=eyJjYXJkQ29udGV4dCI6eyJhdHRyaWJ1dGVzIjp7InZhbHVlQ2FsbG91dCI6eyJtdWx0aVZhbHVlZEF0dHJpYnV0ZSI6eyJrZXkiOiJ2YWx1ZUNhbGxvdXQiLCJpbmZlcmVuY2VUeXBlIjoiVkFMVUVfQ0FMTE9VVCIsInZhbHVlcyI6WyJGcm9tIOKCuTE1Mjk5Il0sInZhbHVlVHlwZSI6Ik1VTFRJX1ZBTFVFRCJ9fSwidGl0bGUiOnsibXVsdGlWYWx1ZWRBdHRyaWJ1dGUiOnsia2V5IjoidGl0bGUiLCJpbmZlcmVuY2VUeXBlIjoiVElUTEUiLCJ2YWx1ZXMiOlsiU2Ftc3VuZyBXYXRjaCA0Il0sInZhbHVlVHlwZSI6Ik1VTFRJX1ZBTFVFRCJ9fSwiaGVyb1BpZCI6eyJzaW5nbGVWYWx1ZUF0dHJpYnV0ZSI6eyJrZXkiOiJoZXJvUGlkIiwiaW5mZXJlbmNlVHlwZSI6IlBJRCIsInZhbHVlIjoiU01XR0Q3TU5XSEhQS0dGMyIsInZhbHVlVHlwZSI6IlNJTkdMRV9WQUxVRUQifX19fX0%3D&fm=neo%2Fmerchandising&iid=M_243c75a5-1312-4054-8d74-6f03ca0efbf8_30.3M7DSFR7VVDV&ppt=hp&ppn=homepage&ssid=cwt4v44m280000001656672341575&otracker=hp_omu_Best%2Bof%2BElectronics_1_30.dealCard.OMU_3M7DSFR7VVDV_17&otracker1=hp_omu_PINNED_neo%2Fmerchandising_Best%2Bof%2BElectronics_NA_dealCard_cc_1_NA_view-all_17&cid=3M7DSFR7VVDV")


source = driver.execute_script("return document.body.innerHTML")

# =======================================================================

documentObjectModel = etree.HTML(source)
tags = documentObjectModel.xpath("//*")
# print(tags)

classset = set()
for tag in tags:

  div = etree.tostring(tag).decode('utf-8')
  el = lxml.html.fromstring(div)
  cls = el.get('class')
#   print(cls)

  ipath = "(//*[@class='"+str(cls)+"']//img)"
  cpath = "(//*[@class='"+str(cls)+"'])"
 
  classlen = len(documentObjectModel.xpath(cpath))
  imglen = len(documentObjectModel.xpath(ipath))

  if ((classlen >=3) & (imglen >=3)):
    classset.add(el.get('class'))
print(len(classset),classset)

parset = set()
pardict = {}
pdict = {}
pcdict = {}
partag = set()
for cls in classset:
  ppath = "//*[@class='"+cls+"']/.."
  parents = documentObjectModel.xpath(ppath)
  for par in parents:
    parstr = etree.tostring(par).decode('utf-8')
    pel = lxml.html.fromstring(parstr)
    pcls = pel.get('class')
    parimg = "//*[@class='"+str(pcls)+"']//img"
    parcnt = "//*[@class='"+str(pcls)+"']"
    pdict[pcls] = cls
    if ((len(documentObjectModel.xpath(parimg)))>3):
      parset.add(pcls)
      partag.add(par.tag)
      pardict[pcls] = par.tag
      pcdict[pcls] = cls

parset = (parset - (parset & classset))
print(parset)
for ele in parset:
  print(pardict[ele],pcdict[ele])