# tests/test_app.py
import pytest
from app import create_app
import json

@pytest.fixture
def client():
    app = create_app()
    # enable testing mode
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_hello_status_code(client):
    resp = client.get("/hello")
    assert resp.status_code == 200

def test_hello_json_body(client):
    resp = client.get("/hello")
    data = resp.get_json()
    assert isinstance(data, dict)
    assert data.get("message") == "hello, world!"
