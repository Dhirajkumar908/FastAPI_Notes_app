from fastapi import APIRouter
from models.note import *
from config.db import *
from schemas.notes_S import *
from typing import Union
from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

templates=Jinja2Templates(directory="templates")

note= APIRouter()

@note.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    docs=conn.Notes.notes.find({})
    newdata=[]
    for doc in docs:
       newdata.append({
           "id":doc["_id"],
           "title":doc["title"],
           "desc":doc["desc"],
        "Is_important":doc["Is_important"]
       })
    return templates.TemplateResponse(request=request, name="index.html", context={"newdata":newdata})

@note.post("/",  response_class=HTMLResponse)
async def create_note(request:Request):
    form=await request.form()
    formDict=dict(form)
    formDict["Is_important"]= True if formDict.get("Is_important")=="on" else False
    note=conn.Notes.notes.insert_one(dict(formDict))

    docs=conn.Notes.notes.find({})
    newdata=[]
    for doc in docs:
       newdata.append({
           "id":doc["_id"],
           "title":doc["title"],
           "desc":doc["desc"],
        "Is_important":doc["Is_important"]
       })
    
    return templates.TemplateResponse(request=request, name="index.html", context={"message": "Note created successfully","newdata":newdata})