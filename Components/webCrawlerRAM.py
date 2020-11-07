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
        'speed': r.html.xpath('//*[@id="product-page"]/section/div[2]/section[2]/div/div[1]/div[2]/div[1]/section/div/div/h2', first = True).text,
        'modules': r.html.xpath('//*[@id="product-page"]/section/div[2]/section[2]/div/div[1]/div[3]/div[4]/div/p', first = True).text,
    }
    p = product['price']
    p = p.replace('$','')
    p = float(p)

    f = open("Components/Tables/RAM.csv","a+")
    sys.stdout = f
    print(product['name'],p, product['manufactuer'], product['speed'], product['modules'], sep="|")
    f.close()
    sys.stdout = original
    return product

if os.path.isfile("Components/Tables/RAM.csv"):
    os.remove("Components/Tables/RAM.csv")

URLS = [
        "https://pcpartpicker.com/product/p6RFf7/corsair-memory-cmk16gx4m2b3200c16",
        "https://pcpartpicker.com/product/QDhKHx/corsair-vengeance-rgb-pro-16gb-2-x-8gb-ddr4-3200-memory-cmw16gx4m2c3200c16",
        "https://pcpartpicker.com/product/NyTPxr/corsair-vengeance-rgb-pro-32gb-2-x-16gb-ddr4-3200-memory-cmw32gx4m2c3200c16",
        "https://pcpartpicker.com/product/VNJtt6/corsair-16-gb-2-x-8-gb-ddr4-3600-memory-cmk16gx4m2d3600c18",
        "https://pcpartpicker.com/product/2TFKHx/crucial-ballistix-16-gb-2-x-8-gb-ddr4-3600-memory-bl2k8g36c16u4b",
        "https://pcpartpicker.com/product/XJYWGX/gskill-aegis-8gb-1-x-8gb-ddr4-3000-memory-f4-3000c16s-8gisb",
        "https://pcpartpicker.com/product/6JRzK8/adata-xpg-z1-16gb-2-x-8gb-ddr4-3000-memory-ax4u300038g16-drz",
        "https://pcpartpicker.com/product/hFdrxr/gskill-trident-z-neo-64-gb-4-x-16-gb-ddr4-3600-memory-f4-3600c16q-64gtznc",
        "https://pcpartpicker.com/product/3yQG3C/corsair-vengeance-rgb-pro-32gb-4-x-8gb-ddr4-3200-memory-cmw32gx4m4c3200c16",
        "https://pcpartpicker.com/product/pyzkcf/gskill-trident-z-royal-16-gb-2-x-8-gb-ddr4-3200-memory-f4-3200c16d-16gtrs",
        "https://pcpartpicker.com/product/tW8j4D/corsair-vengeance-rgb-pro-64gb-4-x-16gb-ddr4-3200-memory-cmw64gx4m4c3200c16w",
        "https://pcpartpicker.com/product/YcTzK8/kingston-hyperx-fury-rgb-16-gb-2-x-8-gb-ddr4-3200-memory-hx432c16fb3ak216"
        ]

URLS_length = len(URLS)

for i in range(URLS_length):
    getGPU(URLS[i])