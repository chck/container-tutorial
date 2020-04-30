from fastapi import FastAPI
import os
import joblib
import shutil
import tempfile
import urllib.request

app = FastAPI()

with urllib.request.urlopen(os.environ["MODEL_PATH"]) as response:
    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        shutil.copyfileobj(response, tmp_file)

model = joblib.load(tmp_file.name)

@app.get("/")
def root():
    return {"model": model.__class__.__name__}
