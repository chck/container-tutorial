from fastapi import FastAPI
import os
import joblib
import shutil
from tempfile import NamedTemporaryFile
from urllib.request import urlopen
from pydantic import BaseModel
import numpy as np
from sklearn import datasets

app = FastAPI()


with urlopen(os.environ["MODEL_PATH"]) as response:
    with NamedTemporaryFile(delete=False) as tmp_file:
        shutil.copyfileobj(response, tmp_file)

model = joblib.load(tmp_file.name)
iris_targets = datasets.load_iris().target_names
estimator_version = "v1"

class Feature(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

@app.get("/")
async def root():
    return dict(estimator_version=estimator_version)

@app.post("/predict")
async def predict(feature: Feature):
    x = np.array(list(feature.dict().values()))
    y_pred = model.predict(np.expand_dims(x, axis=0), num_iteration=model.best_iteration)
    label_pred = iris_targets[np.argmax(y_pred, axis=1)][0]
    return dict(prediction=label_pred)

