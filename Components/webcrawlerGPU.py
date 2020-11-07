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
        'price': r.html.xpath('//*[@id="prices"]/table/tbody/tr/td[2]',first =True).text,
        'manufactuer': r.html.xpath('//*[@id="product-page"]/section/div[2]/section/div/div[1]/div[4]/div[1]/div/p',first =True).text,
        'chipset': r.html.xpath('//*[@id="product-page"]/section/div[2]/section/div/div[1]/div[4]/div[3]/div/p', first = True).text,
        'memory': r.html.xpath('//*[@id="product-page"]/section/div[2]/section/div/div[2]/div[4]/div[4]/div/p', first = True).text,
        'boostclock': r.html.xpath('//*[@id="product-page"]/section/div[2]/section/div/div[2]/div[4]/div[7]/div/p', first = True).text,
        'coreclock': r.html.xpath('//*[@id="product-page"]/section/div[2]/section/div/div[2]/div[4]/div[6]/div/p', first = True).text
    }

    f = open("Tables/GPU.csv","a+")
    sys.stdout = f
    print(product['name'],product['price'], product['manufactuer'], product['chipset'], product['memory'], product['boostclock'], product['coreclock'], sep="|")
    f.close()
    sys.stdout = original
    return product

if os.path.isfile("Tables/GPU.csv"):
    os.remove("Tables/GPU.csv")

URLS = [
        "https://pcpartpicker.com/product/MYMwrH/msi-geforce-gtx-1660-6-gb-ventus-xs-oc-video-card-gtx-1660-ventus-xs-6g-oc",
        "https://pcpartpicker.com/product/6kdrxr/gigabyte-radeon-rx-5700-xt-8-gb-gaming-oc-video-card-gv-r57xtgaming-oc-8gd",
        "https://pcpartpicker.com/product/Z3wkcf/msi-geforce-gtx-1660-super-6-gb-ventus-xs-oc-video-card-gtx-1660-super-ventus-xs-oc",
        "https://pcpartpicker.com/product/KX66Mp/gigabyte-geforce-rtx-2060-6-gb-oc-video-card-gv-n2060oc-6gd",
        "https://pcpartpicker.com/product/fDWBD3/gigabyte-geforce-rtx-3080-10-gb-aorus-master-video-card-gv-n3080aorus-m-10gd",
        "https://pcpartpicker.com/product/QjpmP6/powercolor-radeon-rx-5700-xt-8-gb-video-card-axrx-5700xt-8gbd6-3dh",
        "https://pcpartpicker.com/product/Bc3H99/gigabyte-geforce-rtx-2060-6-gb-windforce-oc-video-card-gv-n2060wf2oc-6gd-r2",
        "https://pcpartpicker.com/product/W7vqqs/asus-geforce-gtx-1660-super-6-gb-strix-gaming-advanced-video-card-rog-strix-gtx1660s-a6g-gaming",
        "https://pcpartpicker.com/product/Z7gzK8/msi-geforce-rtx-2080-ti-11gb-gaming-x-trio-video-card-rtx-2080-ti-gaming-x-trio",
        "https://pcpartpicker.com/product/sZWBD3/gigabyte-radeon-rx-580-8-gb-gaming-8g-video-card-gv-rx580gaming-8gd-rev20",
        "https://pcpartpicker.com/product/ctLwrH/msi-radeon-rx-5600-xt-6-gb-gaming-x-video-card-radeon-rx-5600-xt-gaming-x",
        "https://pcpartpicker.com/product/MnfFf7/gigabyte-geforce-rtx-3090-24-gb-aorus-master-video-card-gv-n3090aorus-m-24gd"
        ]

URLS_length = len(URLS)

for i in range(URLS_length):
    getGPU(URLS[i])