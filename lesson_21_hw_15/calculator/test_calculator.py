import pytest
from httpx import AsyncClient
from sanic import Sanic
from sanic.response import json
from unittest.mock import patch, AsyncMock

from .server import calculator

@pytest.fixture
def test_app():
    return TestClient(app)

