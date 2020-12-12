from os import sep
from os.path import isfile
from sys import path
from typing import Tuple
from requests_html import HTMLSession
import os
import os.path
import sys

def getGPU(url):
    s = HTMLSession()
    r = s.get(url)
    r.html.render(sleep=1)

    product = {
        'name': r.html.xpath('//*[@id="product-page"]/section/div[1]/section/h1',first=True).text,
        'price': r.html.xpath('//*[@id="prices"]/table/tbody/tr[1]/td[2]',first =True).text
    }
    p = product['price']
    p = p.replace('$','')
    p = float(p)
    print(p)
    print(p+1)

getGPU("https://pcpartpicker.com/product/6Cyqqs/nzxt-h510-atx-mid-tower-case-ca-h510b-w1")