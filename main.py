from typing import Union

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pymongo import MongoClient


app=FastAPI()

conn=MongoClient("mongodb+srv://dhirajkmar2:lSSVrNFXxMYTIqKP@dk-cluster.jnct1tu.mongodb.net")



app.mount("/static", StaticFiles(directory="static"), name="static")


templates=Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    docs=conn.Notes.notes.find({})
    newdata=[]
    for doc in docs:
       newdata.append(doc)
    return templates.TemplateResponse(request=request, name="index.html", context={"newdata":newdata})


@app.get("/item/{item_id}")
def read_item(item_id:int, q:Union[str, None]=None):
    return {"item_id":item_id, "q":q}
