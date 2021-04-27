# import sys
# import os
# from os import path
import requests
from bs4 import BeautifulSoup
import re
# import time
# import json
# import csv

# Initial URL to target
def download_url(target_url):
    URL = target_url

    response = requests.get(URL)
    print(response)
    if re.search('^[2-3][0-9][0-9]$', response.status) is not None:
        print('Success')
    elif response.status == '404':
        raise Exception(f'404 Error received for URL: {URL}')
    elif re.search('^[4-5][0-9][0-9]$', response.status) is not None:
        raise Exception(f'Error received for URL: {URL}')


