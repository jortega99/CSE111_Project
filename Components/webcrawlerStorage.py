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
        'manufactuer': r.html.xpath('//*[@id="product-page"]/section/div[2]/section/div/div[1]/div[3]/div[1]/div/p',first =True).text,
        'capacity': r.html.xpath('//*[@id="product-page"]/section/div[2]/section/div/div[1]/div[3]/div[3]/div/p',first =True).text,
        'type': r.html.xpath('//*[@id="product-page"]/section/div[2]/section/div/div[1]/div[3]/div[5]/div/p', first = True).text,
        'cache': r.html.xpath('//*[@id="product-page"]/section/div[2]/section/div/div[1]/div[3]/div[6]/div/p', first = True).text,
    }

    f = open("Components/Tables/Storage.csv","a+")
    sys.stdout = f
    print(product['name'],product['price'], product['manufactuer'], product['capacity'], product['type'], product['cache'], sep="|")
    f.close()
    sys.stdout = original
    return product

if os.path.isfile("Components/Tables/Storage.csv"):
    os.remove("Components/Tables/Storage.csv")

URLS = [
        "https://pcpartpicker.com/product/mwrYcf/seagate-barracuda-computer-2-tb-35-7200rpm-internal-hard-drive-st2000dm008",
        "https://pcpartpicker.com/product/JLdxFT/samsung-970-evo-10tb-m2-2280-solid-state-drive-mz-v7e1t0baw",
        "https://pcpartpicker.com/product/MwW9TW/western-digital-internal-hard-drive-wd10ezex",
        "https://pcpartpicker.com/product/pxKcCJ/crucial-p1-1tb-m2-2280-solid-state-drive-ct1000p1ssd8",
        "https://pcpartpicker.com/product/yzfhP6/samsung-860-evo-1tb-25-solid-state-drive-mz-76e1t0bam",
        "https://pcpartpicker.com/product/Fv8j4D/samsung-970-evo-plus-2-tb-m2-2280-nvme-solid-state-drive-mz-v7s2t0bam",
        "https://pcpartpicker.com/product/btDzK8/kingston-a400-240gb-25-solid-state-drive-sa400s37240g",
        "https://pcpartpicker.com/product/DDWBD3/samsung-980-pro-1-tb-m2-2280-nvme-solid-state-drive-mz-v8p1t0bam",
        "https://pcpartpicker.com/product/dGHRsY/western-digital-black-4tb-35-7200rpm-internal-hard-drive-wd4005fzbx",
        "https://pcpartpicker.com/product/vXH8TW/seagate-ironwolf-pro-4-tb-35-7200rpm-internal-hard-drive-st4000ne001",
        "https://pcpartpicker.com/product/bpjJ7P/adata-su635-240-gb-25-solid-state-drive-asu635ss-240gq-r",
        "https://pcpartpicker.com/product/LFZzK8/crucial-bx500-1-tb-25-solid-state-drive-ct1000bx500ssd1"
        ]

URLS_length = len(URLS)

for i in range(URLS_length):
    getGPU(URLS[i])