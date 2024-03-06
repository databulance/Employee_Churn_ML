import numpy as np
import pandas as pd
import joblib

class PrepProcessor:
    # You can add any preprocessing methods you need here
    pass

# Assuming 'columns' is a list of column names you want to use
columns = ['number_project', 'overworked', 'last_evaluation', 'tenure']

def load_model(model_path):
    with open(model_path, 'rb') as model_file:
        model = joblib.load(model_file)
    return model
