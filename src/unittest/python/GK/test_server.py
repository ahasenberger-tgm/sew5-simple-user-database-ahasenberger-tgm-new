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

def test_updateuserwithemail(client):
    res = client.get('/useradd?email=ahasenberger@student.tgm.ac.at&username=ahasenberger')
    res = client.get('userupdate?email=ahasenbergeeeeer@student.tgm.ac.at&userid=15&username=ahuahuahauhau')
    assert res.status_code == 200

def test_updateuserwithusername(client):
    res = client.get('/useradd?email=ahasenberger@student.tgm.ac.at&username=ahasenberger')
    res = client.get('userupdate?username=ahasenbergeeeeer@student.tgm.ac.at&userid=15&email=haaha@hotmail.com')
    assert res.status_code == 200

def test_adduserUsernameTooShort(client):
    res = client.get('useradd?username=hae&email=ahasenberger@student.tgm.ac.at')
    assert res.status_code == 422

def test_adduserUsernameTooLong(client):
    res = client.get('useradd?username=hgggggggggggggggvreevevvverggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggae&email=ahasenberger@student.tgm.ac.at')
    assert res.status_code == 422

def test_adduserEmailInvalid(client):
    res = client.get('useradd?username=HASEEEEEEE&email=ahasenbergertgmmailmail')
    assert res.status_code == 422

def test_updateuserUsernameTooLong(client):
    res = client.get('/useradd?email=ahasenberger@student.tgm.ac.at&username=ahasenberger')
    res = client.get('userupdate?username=ahasenbergjojijojojjojojojojojojojjojjojojjojojojojojojojojojojojojojojojojojojojojojojojojojojojojojjojojojojojojojojojojojojoeetralalala&userid=15&email=haaha@hotmail.com')
    assert res.status_code == 422

def test_updateuserUsernameTooShort(client):
    res = client.get('/useradd?email=ahasenberger@student.tgm.ac.at&username=ahasenberger')
    res = client.get('userupdate?username=abc&userid=15&email=haaha@hotmail.com')
    assert res.status_code == 422

def test_updateuserEmailInvalid(client):
    res = client.get('/useradd?email=ahasenberger@student.tgm.ac.at&username=ahasenberger')
    res = client.get('userupdate?username=ahasenberger-tgm&userid=15&email=haaha@@@hotmail.com')
    assert res.status_code == 422

def test_adduserNoUsername(client):
    res = client.get('useradd?username=&email=ahasenberger@student.tgm.ac.at')
    assert res.status_code == 422

def test_adduserNoEmail(client):
    res = client.get('useradd?username=abcdfeg&email=')
    assert res.status_code == 422

def test_adduserNoUsernameAndNoEmail(client):
    res = client.get('useradd?username=&email=')
    assert res.status_code == 422

def test_adduserInvalidEmailAndUsernameTooLong(client):
    res = client.get('useradd?username=jjjjjjjjjjjjjjjjjjjjjjjjdjdjdjjdijijijijijijijijijijijijijijijijijijijijijijijijijijijijijijijijijijijijijijijijijijijijijijijijijijijijijijijijijijijijijijijijijijiji&email=ahasenberger')
    assert res.status_code == 422

def test_adduserInvalidEmailAndUsernameTooShort(client):
    res = client.get('useradd?username=j&email=ahasenberger')
    assert res.status_code == 422

def test_updateuserNoUsernameNoEmail(client):
    res = client.get('/useradd?email=ahasenberger@student.tgm.ac.at&username=ahasenberger')
    res = client.get('userupdate?username=&userid=15&email=')
    assert res.status_code == 422