import sys
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
    try:
        response = requests.get(target_url, verify=False)
    except:
        raise Exception(f'unable to download {target_url}')
        log(f'response received was: {response.status_code}, {response.text}, {response.url}')
    else:    
        if int(response.status_code) >= 200 and int(response.status_code) < 400:
            return response
        elif int(response.status_code) == 404:
            raise Exception(f'404 Error received for URL: {target_url}')
        elif int(response.status_code) >= 400:
            raise Exception(f'Error received for URL: {target_url}, code: {response.status_code}')

def extract_links_and_title(html_page):
    soup = BeautifulSoup(html_page, 'html.parser')

    links = []
    for anchor in soup.find_all("a"):
        try:
            if anchor['href'][0] == 'h':
                links.append(anchor['href'])
        except Exception as error:
            log(str(error))
    title = soup.find("title")
    if title is not None:
        title = title.text.strip()
    return (links, title)

def generate_page(page_title, link_list):
    page = graph.Page(page_title)
    if link_list is not None:
        for link in link_list:
            page.add_link(link)
    return page

def extract_page_structure(target_url):
    try:
        response = download_url(target_url)
    except Exception as error:
        log(str(error))
        return -1
    else:
        link_list, page_title = extract_links_and_title(response.text)
        page = generate_page(page_title, link_list)

        return page
    
def page_collector(web_graph, max_depth, target_url, domain):
    new_page = extract_page_structure(target_url)
    if new_page != -1:
        novel_links = web_graph.add_page(new_page)
        if max_depth > 0:
            if novel_links is not None:
                for link in novel_links:
                    print(max_depth-1)
                    if domain in link:
                        page_collector(web_graph, max_depth-1, link, domain)
                    else:
                        print(f'Link leads outside the domain {link}')

def generate_web_graph(initial_url, domain):
    max_depth = 3
    web_graph = graph.WebGraph()
    page_collector(web_graph, max_depth, initial_url, domain)
    return web_graph

def log(message):
    with open("linking_structure_log.txt", 'a+', encoding="utf-8") as log_file:
        log_file.write(message)