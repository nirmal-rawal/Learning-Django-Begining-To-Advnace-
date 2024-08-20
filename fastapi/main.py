from typing import Union
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pymongo import MongoClient

# Replace with your correct MongoDB URI if using a remote MongoDB instance
# For local MongoDB, use "mongodb://localhost:27017"
client = MongoClient("mongodb://localhost:27017")

# Replace 'test_database' and 'test_collection' with your database and collection names
db = client['test_database']
collection = db['test_collection']

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def read_items(request: Request):
    # Replace 'notes' with your actual collection name
    docs = collection.find_one({})
    print(docs)
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
