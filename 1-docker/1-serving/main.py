from fastapi import FastAPI
import lightgbm as lgb
from sklearn import datasets
from sklearn.model_selection import train_test_split
import joblib
import numpy as np

app = FastAPI()

model_version = "20210512"
model = joblib.load(f"models/model_{model_version}.pkl.cmp")

@app.get("/")
def root():
    return dict(version=model_version)

@app.get("/predict")
def predict():
    iris = datasets.load_iris()
    x, y = iris.data, iris.target
    _, x_test, _, _ = train_test_split(x, y)
    y_pred = model.predict(x_test, num_iteration=model.best_iteration)
    label_pred = iris.target_names[np.argmax(y_pred, axis=1)[0]]
    return dict(prediction=label_pred)
