## THE COMMON FUNCTIONALITIES WHICH ARE USED IN THE ENTIRE PROJECT
import os
import sys
import numpy as np
import pandas as pd
import dill
from src.exception import CustomException
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

