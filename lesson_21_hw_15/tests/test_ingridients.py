import pytest
import asyncio
from fastapi import FastAPI
from httpx import AsyncClient

from ..ingridients.server import app
from ..ingridients.server import create_storage

@pytest.fixture
def test_cli(loop, app):
    return AsyncClient(app=app, base_url="http://testserver")

@pytest.mark.asyncio
async def test_create_storage(test_cli):
    response = await test_cli.get("/ingridients/test_id")
    assert response.status_code == 200
    assert response.json() == {
        "storage_id": "test_id",
        "ingridient_1": 0.4,
        "ingridient_2": 2,
        "ingridient_3": 3,
        "ingridient_4": 0.4,
    }
