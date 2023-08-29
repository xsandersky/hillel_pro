import json
from unittest.mock import AsyncMock, patch
import pytest
from httpx import Response
from sanic import Sanic
from sanic.testing import SanicTestClient

from  ..calculator.server import app
from ..calculator.server import calculator

@pytest.fixture
def test_cli(loop, app):
    return SanicTestClient(app)

@pytest.fixture
def mock_httpx_get():
    with patch('calculator.server.httpx.AsyncClient.get') as mock_get:
        yield mock_get

@pytest.fixture
def mock_httpx_response():
    response_data = {
        "storage_id": "test_id",
        "ingridient_1": 0.4,
        "ingridient_2": 2,
        "ingridient_3": 3,
        "ingridient_4": 0.4,
    }
    response = Response(json=response_data)
    return response

async def test_calculator_endpoint(test_cli, mock_httpx_get, mock_httpx_response):
    mock_httpx_get.return_value = AsyncMock(return_value=mock_httpx_response)

    data = {
        "storage_id": "test_id"
    }

    response = await test_cli.post("/calculator", json=data)
    assert response.status == 200
    assert await response.json() == {"Quantity of bread": 4.0}

async def test_calculator_endpoint_invalid_storage(test_cli):
    data = {
        "storage_id": "invalid_id"
    }

    response = await test_cli.post("/calculator", json=data)
    assert response.status == 200
    assert await response.json() == {
        "errors": [{"message": "There is no such storage.", "code": "1000"}]
    }
