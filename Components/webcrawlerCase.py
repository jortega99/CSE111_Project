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
        'formfactor': r.html.xpath('//*[@id="product-page"]/section/div[2]/section[2]/div/div[1]/div[3]/div[3]/div/p',first =True).text,
    }

    p = product['price']
    p = p.replace('$','')
    p = float(p)

    f = open("Components/Tables/Case.csv","a+")
    sys.stdout = f
    print('C_13',product['name'],p, product['manufactuer'], product['formfactor'], sep="|")
    f.close()
    sys.stdout = original
    return product

URLS = [
        "https://pcpartpicker.com/product/YcCFf7/rosewill-prism-s-lite-atx-mid-tower-case-prism-s-black-lite"
        ]

URLS_length = len(URLS)

for i in range(URLS_length):
    getGPU(URLS[i])