from os import sep
from os.path import isfile
from sys import path
from typing import Tuple
from requests_html import HTMLSession
import os
import os.path
import sys

original = sys.stdout

def getCPU(url):
    s = HTMLSession()
    r = s.get(url)
    r.html.render(sleep=1)

    product = {
        'name': r.html.xpath('//*[@id="product-page"]/section/div[1]/section/h1',first=True).text,
        'price': r.html.xpath('//*[@id="prices"]/table/tbody/tr[1]/td[2]',first =True).text,
        'manufactuer': r.html.xpath('//*[@id="product-page"]/section/div[2]/section/div/div[1]/div[4]/div[1]/div/p',first =True).text,
        'corecount': r.html.xpath('//*[@id="product-page"]/section/div[2]/section/div/div[1]/div[4]/div[3]/div/p',first = True).text,
        'coreclock': r.html.xpath('//*[@id="product-page"]/section/div[2]/section/div/div[1]/div[4]/div[4]/div/p',first = True).text,
        'boostclock': r.html.xpath('//*[@id="product-page"]/section/div[2]/section/div/div[1]/div[4]/div[5]/div/p',first=True).text    
    }
    p = product['price']
    p = p.replace('$','')
    p = float(p)

    f = open("Components/Tables/CPU.csv","a+")
    sys.stdout = f
    print(product['name'], p, product['manufactuer'], product['corecount'], product['coreclock'], product['boostclock'], sep="|")
    f.close()
    sys.stdout = original
    return product

if os.path.isfile("Components/Tables/CPU.csv"):
    os.remove("Components/Tables/CPU.csv")

URLS = ["https://pcpartpicker.com/product/9nm323/amd-ryzen-5-3600-36-thz-6-core-processor-100-100000031box",
        "https://pcpartpicker.com/product/QKJtt6/amd-ryzen-7-3700x-36-ghz-8-core-processor-100-100000071box",
        "https://pcpartpicker.com/product/9nm323/amd-ryzen-5-3600-36-thz-6-core-processor-100-100000031box",
        "https://pcpartpicker.com/product/3WYLrH/amd-ryzen-5-3600x-38-thz-6-core-processor-100-100000022box",
        "https://pcpartpicker.com/product/bddxFT/amd-ryzen-7-2700x-37ghz-8-core-processor-yd270xbgafbox",
        "https://pcpartpicker.com/product/bddxFT/amd-ryzen-7-2700x-37ghz-8-core-processor-yd270xbgafbox",
        #the ones that work ^^^^^^^^
        #"https://pcpartpicker.com/product/J8drxr/amd-ryzen-3-3200g-36-ghz-quad-core-processor-yd3200c5fhbox"
        #"https://pcpartpicker.com/product/t7CFf7/amd-ryzen-9-3950x-35-ghz-16-core-processor-100-100000051wof",
        "https://pcpartpicker.com/product/WtyV3C/intel-core-i7-9700k-36ghz-8-core-processor-bx80684i79700k",
        "https://pcpartpicker.com/product/yhxbt6/intel-core-i7-10700k-38-ghz-8-core-processor-bx8070110700k",
        "https://pcpartpicker.com/product/cwFKHx/intel-core-i9-10900k-37-ghz-10-core-processor-bx8070110900k",
        "https://pcpartpicker.com/product/jHZFf7/intel-core-i9-9900k-36ghz-8-core-processor-bx80684i99900k",
        #"https://pcpartpicker.com/product/YTbwrH/intel-core-i3-9100f-36-ghz-quad-core-processor-bx80684i39100f",
        "https://pcpartpicker.com/product/T47v6h/intel-core-i5-9400f-29-ghz-6-core-processor-bx80684i59400f",
        "https://pcpartpicker.com/product/X8snTW/intel-core-i5-10400-29-ghz-6-core-processor-bx8070110400",
        #"https://pcpartpicker.com/product/qtqBD3/intel-core-i3-10100-36-ghz-quad-core-processor-bx8070110100"
        ]
URLS_length = len(URLS)

for i in range(URLS_length):
    getCPU(URLS[i])
