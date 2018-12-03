import pytest
import server.main
from flask import url_for
from flask import Flask
from server import Rest

@pytest.fixture
def client():
    Rest.app.testing = True
    client = Rest.app.test.client()
    yield client

def test_ping(client):
    res = client.get('/userget')
    assert res.status_code == 200

def test_adduser(client):
    res = client.get('/useradd?email=ahasenberger@student.tgm.ac.at&username=ahasenberger')
    assert res.status_code == 200

def test_deleteuser(client):
    res = client.get('/userdelete?userid=2&username=ahasenberger&email=ahasenberger@student.tgm.ac.at')
    assert res.status_code == 200