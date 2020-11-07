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
        'manufactuer': r.html.xpath('//*[@id="product-page"]/section/div[2]/section[2]/div/div[1]/div[2]/div[1]/div/p',first =True).text,
        'socket': r.html.xpath('//*[@id="product-page"]/section/div[2]/section[2]/div/div[1]/div[2]/div[3]/div/p', first = True).text,
        'formfactor': r.html.xpath('//*[@id="product-page"]/section/div[2]/section[2]/div/div[1]/div[2]/div[4]/div/p', first = True).text,
    }
    p = product['price']
    p = p.replace('$','')
    p = float(p)

    f = open("Components/Tables/MB.csv","a+")
    sys.stdout = f
    print(product['name'],p, product['manufactuer'], product['socket'], product['formfactor'], sep="|")
    f.close()
    sys.stdout = original
    return product

if os.path.isfile("Components/Tables/MB.csv"):
    os.remove("Components/Tables/MB.csv")

URLS = [
        "https://pcpartpicker.com/product/jcYQzy/msi-b450-tomahawk-max-atx-am4-motherboard-b450-tomahawk-max",
        "https://pcpartpicker.com/product/hpRzK8/gigabyte-b450m-ds3h-micro-atx-am4-motherboard-b450m-ds3h",
        "https://pcpartpicker.com/product/dmGnTW/asus-tuf-gaming-x570-plus-wi-fi-atx-am4-motherboard-tuf-gaming-x570-plus-wi-fi",
        "https://pcpartpicker.com/product/qpL48d/msi-z390-a-pro-atx-lga1151-motherboard-z390-a-pro",
        "https://pcpartpicker.com/product/vFhmP6/asus-rog-strix-b550-f-gaming-wi-fi-atx-am4-motherboard-rog-strix-b550-f-gaming-wi-fi",
        "https://pcpartpicker.com/product/J9PgXL/asus-rog-strix-z490-e-gaming-atx-lga1200-motherboard-rog-strix-z490-e-gaming",
        "https://pcpartpicker.com/product/2k3H99/asus-prime-z390-a-atx-lga1151-motherboard-prime-z390-a",
        "https://pcpartpicker.com/product/6FvZxr/asus-prime-a320m-k-micro-atx-am4-motherboard-prime-a320m-k",
        "https://pcpartpicker.com/product/ZGDJ7P/gigabyte-b450-i-aorus-pro-wifi-mini-itx-am4-motherboard-b450-i-aorus-pro-wifi",
        "https://pcpartpicker.com/product/PDsnTW/msi-b550m-pro-vdh-wifi-micro-atx-am4-motherboard-b550m-pro-vdh-wifi",
        "https://pcpartpicker.com/product/GcfFf7/asus-rog-crosshair-viii-hero-wi-fi-atx-am4-motherboard-rog-crosshair-viii-hero-wi-fi",
        "https://pcpartpicker.com/product/sL7v6h/gigabyte-ga-a320m-s2h-micro-atx-am4-motherboard-ga-a320m-s2h"
        ]

URLS_length = len(URLS)

for i in range(URLS_length):
    getGPU(URLS[i])