import pytest
import unittest
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
    
