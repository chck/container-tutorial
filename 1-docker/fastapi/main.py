from fastapi import FastAPI
import os
import joblib
import shutil
import tempfile
import urllib.request

app = FastAPI()

@app.get("/")
def root():
    return {"Hello": "World"}
