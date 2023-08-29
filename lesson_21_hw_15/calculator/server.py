from uuid import uuid4

import httpx
import requests
from sanic import Sanic
from sanic.request import Request
from sanic.response import HTTPResponse, json

app = Sanic("calculator_app")


@app.post("/calculator")
async def calculator(request: Request) -> HTTPResponse:
    storage_id = request.json["storage_id"]
    async with httpx.AsyncClient() as client:
        response = await client.get(f"http://127.0.0.1:8081/ingridients/{storage_id}")
    if response.json()['storage_id']:
        # value0 = response.json()["ingridient_1"]
        # value1 = response.json()["ingridient_2"]
        # value2 = response.json()["ingridient_3"]
        # value3 = response.json()["ingridient_4"]
        ingridient_keys = ["ingridient_1", "ingridient_2", "ingridient_3", "ingridient_4"]
        values = [response.json()[key] for key in ingridient_keys]
        list_res_for_bread = [values[0] / 0.1, values[1] / 1, values[2] / 0.5, values[3] / 0.2]
        return json({'Quantity of bread': min(list_res_for_bread)})
    else:
        return json(
            {
                "errors": [
                    {"message": "There is no such storage.", "code": "1000"}
                ]
            }
        )
