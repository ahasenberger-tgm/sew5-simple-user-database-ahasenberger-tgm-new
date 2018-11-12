import pytest
import server.main
from flask import url_for
from flask import Flask
from server import api

@pytest.fixture
def client():
    server.main.app.testing = True
    client = server.main.app.test_client()
    yield client

@pytest.fixture
def client():
    api.app.testing = True
    client = api.app.test.client()
    yield client

def test_ping(client):
    res = client.get('/user')
    assert res.status_code == 200