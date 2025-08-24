## THE COMMON FUNCTIONALITIES WHICH ARE USED IN THE ENTIRE PROJECT
import os
import sys
import numpy as np
import pandas as pd
import dill
from src.exception import CustomException
from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV
def save_object(file_path,obj):
    try:
        dir_path=os.path.dirname(file_path)
        os.makedirs(dir_path,exist_ok=True)
        with open(file_path,'wb') as file_obj:
            dill.dump(obj,file_obj)
    except Exception as e:
        raise CustomException(e,sys)
    
#     dir_path = os.path.dirname(file_path)

# Extracts the folder path from the full file path.

# Example: if file_path = "artifacts/model.pkl", then dir_path = "artifacts".

# os.makedirs(dir_path, exist_ok=True)

# Ensures that the directory exists.

# If it doesn’t exist, it will be created.

# exist_ok=True prevents errors if the folder already exists.

# with open(file_path, 'wb') as file_obj:

# Opens the target file in write-binary mode (wb) so you can store binary data (like models or objects).

# dill.dump(obj, file_obj)

# Uses dill (a more powerful alternative to Python’s pickle) to serialize the Python object (obj) and save it into the file.

# This is often used to save ML models, preprocessors, or any Python object

from sklearn.metrics import r2_score
import sys

def evaluate_models(X_train, y_train, X_test, y_test, models, param):
    report = {}
    fitted_models = {}

    for model_name, model in models.items():
        para = param[model_name]

        gs = GridSearchCV(model, para, cv=3, n_jobs=-1, verbose=1)
        gs.fit(X_train, y_train)

        best_model = gs.best_estimator_

        # Safety: ensure fitted
        if not hasattr(best_model, "predict"):
            best_model.fit(X_train, y_train)

        y_train_pred = best_model.predict(X_train)
        y_test_pred = best_model.predict(X_test)

        train_score = r2_score(y_train, y_train_pred)
        test_score = r2_score(y_test, y_test_pred)

        report[model_name] = test_score
        fitted_models[model_name] = best_model   # ✅ store fitted model

    return report, fitted_models

