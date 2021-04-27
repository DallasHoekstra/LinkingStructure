# import sys
# import os
# from os import path
import requests
from bs4 import BeautifulSoup
import re
import WebGraph as graph
# import time
# import json
# import csv

# Initial URL to target
def download_url(target_url):
    response = requests.get(target_url)

    if re.search('^[2-3][0-9][0-9]$', response.status) is not None:
        return response
    elif response.status == '404':
        raise Exception(f'404 Error received for URL: {URL}')
    elif re.search('^[4-5][0-9][0-9]$', response.status) is not None:
        raise Exception(f'Error received for URL: {URL}')

def extract_links(html_page):
    soup = BeautifulSoup(html_page, 'html.parser')

    links = []
    for anchor in soup.find_all("a"):
        links.append(anchor['href'])
    return links

def generate_page(page_title, link_list):
    page = graph.Page(page_title)
    for link in link_list:
        page.add_link(link)
    return page

