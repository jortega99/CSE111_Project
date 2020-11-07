import requests
from bs4 import BeautifulSoup as bs

URL = "https://pcpartpicker.com/product/RnDkcf/nvidia-geforce-rtx-3080-10-gb-founders-edition-video-card-9001g1332530000"
r = requests.get(URL)

soup = bs(r.content, 'html.parser')

first_header = soup.find("div", {"class": "group__content"})
print(first_header)