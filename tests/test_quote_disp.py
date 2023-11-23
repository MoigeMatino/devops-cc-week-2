import pytest
import requests
import requests_mock
from quote_disp.app import app, get_quote



def test_get_quote():
    with requests_mock.Mocker() as mocker:
        mock_quote_url = 'http://web1:5000/quote'
        mock_response_text = 'The way to get started is to quit talking and begin doing. -Walt Disney'
        mocker.get(mock_quote_url, text=mock_response_text)
        quote_result = get_quote()
        assert quote_result == mock_response_text
        
        
    
    
    
    