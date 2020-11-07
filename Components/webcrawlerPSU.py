from os import sep
from os.path import isfile
from sys import path
from typing import Tuple
from requests_html import HTMLSession
import os
import os.path
import sys

original = sys.stdout

def getGPU(url):
    s = HTMLSession()
    r = s.get(url)
    r.html.render(sleep=1)

    product = {
        'name': r.html.xpath('//*[@id="product-page"]/section/div[1]/section/h1',first=True).text,
        'price': r.html.xpath('//*[@id="prices"]/table/tbody/tr[1]/td[2]',first =True).text,
        'manufactuer': r.html.xpath('//*[@id="product-page"]/section/div[2]/section[2]/div/div[1]/div[3]/div[1]/div/p',first =True).text,
        'formfactor': r.html.xpath('//*[@id="product-page"]/section/div[2]/section[2]/div/div[1]/div[3]/div[4]/div/p',first =True).text,
        'wattage': r.html.xpath('//*[@id="product-page"]/section/div[2]/section[2]/div/div[1]/div[3]/div[6]/div/p', first = True).text,
        'efficiency': r.html.xpath('//*[@id="product-page"]/section/div[2]/section[2]/div/div[1]/div[3]/div[5]/div/p', first = True).text,
        'modularity': r.html.xpath('//*[@id="product-page"]/section/div[2]/section[2]/div/div[1]/div[3]/div[8]/div/p', first = True).text
    }
    p = product['price']
    p = p.replace('$','')
    p = float(p)

    f = open("Components/Tables/PSU.csv","a+")
    sys.stdout = f
    print(product['name'],p, product['manufactuer'], product['formfactor'], product['wattage'], product['efficiency'], product['modularity'], sep="|")
    f.close()
    sys.stdout = original
    return product

if os.path.isfile("Components/Tables/PSU.csv"):
    os.remove("Components/Tables/PSU.csv")

URLS = [
        "https://pcpartpicker.com/product/6Y66Mp/corsair-rm-2019-750-w-80-gold-certified-fully-modular-atx-power-supply-cp-9020195-na",
        "https://pcpartpicker.com/product/jtm323/corsair-rm-2019-850-w-80-gold-certified-fully-modular-atx-power-supply-cp-9020196-na",
        "https://pcpartpicker.com/product/8P7CmG/evga-bq-500w-80-bronze-certified-semi-modular-atx-power-supply-110-bq-0500-k1",
        "https://pcpartpicker.com/product/J7F48d/cooler-master-mwe-gold-650-w-80-gold-certified-fully-modular-atx-power-supply-mpy-6501-afaag-us",
        "https://pcpartpicker.com/product/kCtQzy/evga-br-500w-80-bronze-certified-atx-power-supply-100-br-0500-k1",
        "https://pcpartpicker.com/product/R2mxFT/corsair-power-supply-cp9020103na",
        "https://pcpartpicker.com/product/Wbhj4D/thermaltake-smart-500w-80-certified-atx-power-supply-ps-spd-0500npcwus-w",
        "https://pcpartpicker.com/product/xDMwrH/evga-br-450w-80-bronze-certified-atx-power-supply-100-br-0450-k1",
        "https://pcpartpicker.com/product/Rxprxr/seasonic-s12iii-650-w-80-bronze-certified-atx-power-supply-ssr-650gb3",
        "https://pcpartpicker.com/product/y88H99/evga-supernova-g3-650w-80-gold-certified-fully-modular-atx-power-supply-220-g3-0650",
        "https://pcpartpicker.com/product/PVzZxr/corsair-txm-gold-650w-80-gold-certified-semi-modular-atx-power-supply-cp-9020132-na",
        "https://pcpartpicker.com/product/6RTrxr/thermaltake-smart-600w-80-certified-semi-modular-atx-power-supply-ps-spd-0600npcwus-w"
        ]

URLS_length = len(URLS)

for i in range(URLS_length):
    getGPU(URLS[i])