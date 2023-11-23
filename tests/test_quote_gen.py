import pytest
from quote_gen.app import app

@pytest.fixture
def client():    

    yield app.test_client()


quotes = [
        "The greatest glory in living lies not in never falling, but in rising every time we fall. -Nelson Mandela",
        "The way to get started is to quit talking and begin doing. -Walt Disney",
        "Your time is limited, so don't waste it living someone else's life. Don't be trapped by dogma – which is living with the results of other people's thinking. -Steve Jobs",
        "If life were predictable it would cease to be life, and be without flavor. -Eleanor Roosevelt",
        "If you look at what you have in life, you'll always have more. If you look at what you don't have in life, you'll never have enough. -Oprah Winfrey",
        "If you set your goals ridiculously high and it's a failure, you will fail above everyone else's success. -James Cameron",
    ]

def test_home_page_get(client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/' page is requested (GET)
    THEN check that the response is valid
    """ 
    response = client.get('/')
    assert response.status_code == 200
    assert '<h1 style="color: white">Quote Generation Service</h1>' in response.data.decode('utf-8') 


def test_home_page_post(client):
    """
    GIVEN a Flask application configured for testing
    WHEN data is submitted to the '/' page (POST)
    THEN check that the response status code is 405
    """
    response = client.post('/')
    assert response.status_code == 405
    

def test_health_get(client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/health' page is requested (GET)
    THEN check that the response status code is 200 and
    that the correct message is returned
    """
    response = client.get('/health')
    assert response.status_code == 200
    assert response.data.decode() == "healthy"
    
def test_health_post(client):
    """
    GIVEN a Flask application configured for testing
    WHEN data is submitted to the '/health' page (POST)
    THEN check that the response status code is 405
    """
    response = client.post('/health')
    assert response.status_code == 405
    
def test_quote_get(client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/quote' page is requested (GET)
    THEN check that the response status code is 200 and
    that one of the valid quotes is returned
    """    
    response = client.get('/quote')
    assert response.status_code == 200 
    assert response.data.decode() in quotes

def test_quote_post(client):
    """
    GIVEN a Flask application configured for testing
    WHEN data is submitted to the '/quote' page (POST)
    THEN check that the response status code is 405
    """
    response = client.post('/quote')
    assert response.status_code == 405