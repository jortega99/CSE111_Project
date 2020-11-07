from os import sep
from requests_html import HTMLSession

def getCPU(url):
    s = HTMLSession()
    r = s.get(url)
    r.html.render(sleep=1)

    product = {
        'name': r.html.xpath('//*[@id="category_content"]', first = True).text 
    }


    #print(product['name'],product['price'], product['manufactuer'], product['corecount'], product['coreclock'], product['boostclock'], sep="|")
    print(product['name'])
    return product

getCPU('https://pcpartpicker.com/products/cpu/')