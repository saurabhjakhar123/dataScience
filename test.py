from flask import Flask, render_template, request
from urllib.request import urlopen
from bs4 import BeautifulSoup as bs

search_for = "iphone"
comp_url = "https://www.flipkart.com/search?q=" + search_for
url_open = urlopen(comp_url)
read_url = url_open.read()
beautify_url = bs(read_url, 'html.parser')
bigBox = beautify_url.findAll("div", {"class" : "_2kHMtA"})

items_list = []
for i in bigBox:

        items_dict = {}
        
        #title
        title = i.find("div", {'class' : '_4rR01T'}).text
        items_dict["title"] = title

        #rating
        rating = i.find("div", {'class' : '_3LWZlK'}).text
        items_dict["rating"] = rating
        
        #people_count
        people_count = i.find("span", {'class' : '_2_R_DZ'}).text
        items_dict["people_count"] = people_count
        
        #price
        price = i.find("div", {'class' : '_30jeq3 _1_WHN1'}).text
        items_dict["price"] = price

        #product_link
        link = i.find("a", {"class" : "_1fQZEK"})["href"]
        product_link = "https://flipkart.com"+link
        items_dict["product_link"] = product_link 
        

        #key_specifications
        ul_list = i.find("ul", {'class': '_1xgFaf'})
        specs = []
        if ul_list:
            for li in ul_list.find_all('li'):
                specs.append(li.text)
        items_dict["key_specs"] = specs

        items_list.append(items_dict)

# print(items_list)

for item in items_list:
    print(item["key_specs"].end('\n'))