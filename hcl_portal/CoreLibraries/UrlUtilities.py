'''
This file provides the utility to handle the urls
like download the content from given url
'''

import os
from urllib.parse import urlparse
import requests

'''
this function parses the url and returns the file for the resource
'''
def get_file_name_from_url(url):
    url_parsed_data = urlparse(url)
    return os.path.basename(url_parsed_data.path)

'''
this function save the resource pointed by url to local specified path
'''
def save_file_from_url(url,file_name_with_path):
    url_file = requests.get(url)
    with open(file_name_with_path, 'wb') as file:
        file.write(url_file.content)