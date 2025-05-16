import pytest
from fastapi.testclient import TestClient
from fastapi import WebSocket
from websockets.sync.client import connect
import threading
import uvicorn
import time

from main import app

client = TestClient(app)

# Test HTML route
def test_get_root():
    response = client.get("/")
    assert response.status_code == 200
    assert "<title>WebSocket Progress</title>" in response.text
