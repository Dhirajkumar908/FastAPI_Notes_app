from fastapi import FastAPI
from routes.notes import *
from fastapi.staticfiles import StaticFiles


app=FastAPI()
app.include_router(note)

app.mount("/static", StaticFiles(directory="static"), name="static")

