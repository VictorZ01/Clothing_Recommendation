import urllib.request
from selenium import webdriver  
from selenium.common.exceptions import NoSuchElementException  
from selenium.webdriver.common.keys import Keys  
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from sys import platform
import time
import pandas as pd
import urllib
import os 
import shutil





class Parser:
    def __init__(self):
        options=Options()
        options.add_argument("--headless=new")
        self.driver=webdriver.Firefox(options=options)

    def scroll_down(self,downSize):
        height=self.driver.execute_script("return document.body.scrollHeight")
        while True:
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight-"+str(downSize)+");")
            time.sleep(5)
            new_height = self.driver.execute_script("return document.body.scrollHeight")           
            if new_height == height:
                break

            height = new_height

webpage=Parser()
cwd=os.getcwd()

#Uniqlo
 
webpage.driver.get('https://www.uniqlo.com/us/en/search?q=hats') 

response=webpage.scroll_down(1700)
source=webpage.driver.page_source
soup=BeautifulSoup(source,"html.parser")
print("Finished with loading")
pictures=[]
price=[]
bulk=soup.find(attrs={"class":"fr-ec-product-collection fr-ec-product-collection--type-grid fr-ec-product-collection--ecrenewal-grid"})
tiles=bulk.find_all(attrs={"class":"fr-ec-product-tile-resize-wrapper"})


for i in tiles:
    pictures.append(i.find("img").get("src"))
    x=(i.find("div",{"class":"fr-ec-content-alignment fr-ec-content-alignment--direction-row fr-ec-content-alignment--content-flex-start fr-ec-content-alignment--alignment-baseline fr-ec-price__amount"}))
    if x==None:
        x=i.find("div",{"class":"fr-ec-content-alignment fr-ec-content-alignment--direction-row fr-ec-content-alignment--content-flex-start fr-ec-content-alignment--alignment-baseline"})
    text_price=x.text
    price.append(text_price)

if platform=="Windows": 
    path=(cwd+"\\Pictures\\")
else:
    path=(cwd+"//Pictures//")

if not os.path.exists(path):
    os.mkdir(path)
else:
    shutil.rmtree(path) 
    os.makedirs(path)
for i in range(len(price)):
    if platform=="Windows": 
        urllib.request.urlretrieve(str(pictures[i]),cwd+"/Pictures/file{}".format(i)+price[i]+".jpg")
    else:
        urllib.request.urlretrieve(str(pictures[i]),cwd+"/Pictures/file{}".format(i)+price[i]+".jpg")

webpage.driver.quit()

df=pd.DataFrame({"url":pictures,"price":price})
df.to_csv("pictures.csv",index=False,encoding="utf-8")

#Lululemon
#webpage.driver.get("https://shop.lululemon.com/search?Ntt=pants")
#american eagle
#webpage.driver.get("https://www.ae.com/us/en/s/white+pants")
quit()