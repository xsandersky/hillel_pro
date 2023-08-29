from fastapi import FastAPI
from uuid import uuid4
import asyncio

app = FastAPI()

@app.get('/ingridients/{storage_id}')
async def create_storage(storage_id):
    await asyncio.sleep(0.1)
    return {
        'storage_id': str(uuid4()),
        'ingridient_1': 0.4,
        'ingridient_2': 2,
        'ingridient_3': 3,
        'ingridient_4': 0.4,
    }
