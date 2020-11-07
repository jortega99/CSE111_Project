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
    print(product['name'],p, product['manufactuer'], product['formfactor'], sep="|")
    f.close()
    sys.stdout = original
    return product

if os.path.isfile("Components/Tables/Case.csv"):
    os.remove("Components/Tables/Case.csv")

URLS = [
        "https://pcpartpicker.com/product/6Cyqqs/nzxt-h510-atx-mid-tower-case-ca-h510b-w1",
        "https://pcpartpicker.com/product/b7hmP6/nzxt-h510-atx-mid-tower-case-ca-h510b-b1",
        "https://pcpartpicker.com/product/Y6Crxr/fractal-design-meshify-c-atx-mid-tower-case-fd-ca-mesh-c-bko-tg",
        "https://pcpartpicker.com/product/VxRzK8/lian-li-pc-o11dw-atx-full-tower-case-pc-o11dw",
        "https://pcpartpicker.com/product/rnGxFT/cooler-master-masterbox-q300l-microatx-mini-tower-case-mcb-q300l-kann-s00",
        "https://pcpartpicker.com/product/sY9tt6/corsair-275r-airflow-atx-mid-tower-case-cc-9011181-ww",
        "https://pcpartpicker.com/product/kpx2FT/nzxt-h510-elite-atx-mid-tower-case-ca-h510e-w1",
        "https://pcpartpicker.com/product/ycbCmG/corsair-275r-airflow-atx-mid-tower-case-cc-9011182-ww",
        "https://pcpartpicker.com/product/Hwkj4D/lian-li-pc-o11dx-atx-full-tower-case-pc-o11dx",
        "https://pcpartpicker.com/product/kRFKHx/lian-li-lancool-ii-x-atx-mid-tower-case-lancool-ii-x",
        "https://pcpartpicker.com/product/gfn8TW/cooler-master-masterbox-td500-mesh-white-w-controller-atx-mid-tower-case-mcb-d500d-wgnn-s01",
        "https://pcpartpicker.com/product/bCYQzy/corsair-4000d-airflow-atx-mid-tower-case-cc-9011200-ww"
        ]

URLS_length = len(URLS)

for i in range(URLS_length):
    getGPU(URLS[i])