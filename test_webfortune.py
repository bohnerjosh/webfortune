import pytest
from appserver import app as flask_app
from appserver import fortune, cowsay, cowfortune
import os

@pytest.fixture
def app():
    yield flask_app

@pytest.fixture
def client(app):
    return app.test_client()

def test_fortune(app, client):
    # Test to see if fortune is installed
    text = ""
    num = os.system("fortune 1>/dev/null 2>/dev/null") 
    # returns status code, returns 1 if fortune is not installed
    assert num == 0
    
    expected = "<pre>"
    other_expected = "</pre>"
    res = client.get('/fortune/')
    assert res.status_code == 200
    page_output = res.get_data(as_text=True)
    assert expected in page_output
    assert other_expected in page_output

    other_res = client.get('/fortnone/')
    assert other_res.status_code == 404

def test_cowsay(app, client):
    num = os.system("cowsay 1>/dev/null 2>/dev/null")
    # returns status code, returns 1 if fortune is not installed
    assert num == 0
    text = ""
    os.system("rm -rf temp.txt")
    message = 'hello'
    res = client.get('/cowsay/%s/' % message)
    assert res.status_code == 200
    page_output = res.get_data(as_text=True)
    assert message in page_output

    other_res = client.get('/cowsey/%s/' % message)
    assert other_res.status_code == 404

    other_res = client.get('/cowsay/')
    assert other_res.status_code == 404

def test_cowfortune(app, client):
    num = os.system("cowsay 1>/dev/null 2>/dev/null")
    # returns status code, returns 1 if cowsay is not installed
    assert num == 0

    num = os.system("fortune 1>/dev/null 2>/dev/null") 
    # returns status code, returns 1 if fortune is not installed
    assert num == 0

    expected = "<pre>"
    other_expected = "</pre>"
    res = client.get('/cowfortune/')
    assert res.status_code == 200
    page_output = res.get_data(as_text=True)
    assert expected in page_output
    assert other_expected in page_output

    other_res = client.get('/cowfort/')
    assert other_res.status_code == 404

    other_res = client.get('/cowfortune/lhk')
    assert other_res.status_code == 404
