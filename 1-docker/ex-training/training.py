import lightgbm as lgb
import os

from sklearn import datasets
from sklearn.model_selection import train_test_split
import numpy as np
import joblib

iris = datasets.load_iris()
x, y = iris.data, iris.target
x_train, x_test, y_train, y_test = train_test_split(x, y)

train_ds = lgb.Dataset(x_train, y_train)
test_ds = lgb.Dataset(x_test, y_test, reference=train_ds)
lgb_params = dict(
    objective="multiclass",
    num_class=3,
)
model = lgb.train(
    lgb_params,
    train_ds,
    valid_sets=test_ds,
)

y_pred = model.predict(x_test, num_iteration=model.best_iteration)
accuracy = sum(y_test == np.argmax(y_pred, axis=1)) / len(y_test)
print(f"Accuracy: {accuracy:.2f}")

os.makedirs(f"models/v1", exist_ok=True)
joblib.dump(model, f"models/v1/model.pkl.cmp", compress=True)
