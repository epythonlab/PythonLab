from bs4 import BeautifulSoup as bs
import pandas as pd
import requests

# Get Data by category
def get_by_category(base_url):
    
    list_categories =[]
    # send http request and get http response
    http_response = requests.get(base_url)
    # get html content us bs
    html_page = bs(http_response.content, 'html.parser')
    
    categories = content.find("ul", 
                                     {"class":"pypi-trending-packages"}).find("li").findAll('a', {'package-snippet'}).text
    
    
    for cat in categories:
        list_categories.append(cat)
    
    return list_categories
    

# call function get_by_category()
categories = get_by_category('https://pypi.org/')
print(categories)