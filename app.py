from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/order/{order_id}/{products_list}")
def read_item(order_id: int, products_list: str):
    return {"order": order_id, "products_list": products_list}
