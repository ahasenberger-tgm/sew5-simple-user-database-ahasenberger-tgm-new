import pytest

from flask import url_for
from flask import Flask
from server.rest import app

@pytest.fixture
def client():
    app.testing = True
    client = app.test_client()
    yield client

def test_ping(client):
    res = client.get('/')
    assert res.status_code == 200

def test_adduser(client):
    res = client.get('/useradd?email=ahasenberger@student.tgm.ac.at&username=ahasenberger')
    assert res.status_code == 200

def test_deleteuser(client):
    res = client.get('/userdelete?userid=2&username=ahasenberger&email=ahasenberger@student.tgm.ac.at')
    assert res.status_code == 200

def test_getuser(client):
    res = client.get('/userget')
    assert res.status_code == 200