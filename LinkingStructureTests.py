import pytest
import unittest
import os.path
from os import path
from unittest.mock import patch
import LinkingStructure as LS


# def se_echo(*args, **kwargs):
#     if len(args):
#         print(f'called with {args[0]}')
#     else:
#         print('received no positional arguments. Please use the format se_echo(single_argument)')

class Response_Object():
    def __init__(self, *args, **kwargs):
        self.status = kwargs['status']
        self.text = kwargs['data']

def generate_sample_html():
        sample_page = """<html> 
                            <head>
                            </head>
                            <body>
                                <a href="www.google.com">Begin the search!</a>
                            </body> 
                    </html>"""

        f = open('sample_html.html', 'w')
        f.write(sample_page)
        f.close()

@patch("requests.get")
def test_opens_correct_initial_url(mock_requests_get):
    mock_requests_get.return_value = Response_Object(status='200', data='google')
    target_url = "https://www.google.com"

    LS.download_url(target_url)

    mock_requests_get.assert_called()
    mock_requests_get.assert_called_with(target_url)

@pytest.mark.parametrize("status", [("404"), ("400"), ("500")])
@patch("requests.get")
def test_handles_error_codes_correctly(mock_requests_get, status):

    mock_requests_get.return_value = Response_Object(status=status, data='')
    target_url = "https://www.google.com"
    with pytest.raises(Exception):
        LS.download_url(target_url)
    
def test_extract_links_extracts_anchor_tag_hrefs():
    if not path.exists('sample_html.html'):
        generate_sample_html()

    with open('sample_html.html', 'r') as sample_page:
        links = LS.extract_links(sample_page)
        assert links is not None

def test_generate_page_adds_links_and_title():
    link_list = ["www.google.com", "www.giantitp.com", "www.xkcd.com", "www.xkcd.com"]
    page_title = "best websites"

    page = LS.generate_page(page_title, link_list)

    assert page.title == page_title
    assert page.links["www.google.com"] == 1
    assert page.links["www.giantitp.com"] == 1
    assert page.links["www.xkcd.com"] == 2