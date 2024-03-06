import numpy as np
import pandas as pd
import joblib  # Import joblib for loading the model

class PrepProcessor:
    # You can add any preprocessing methods you need here
    pass

# Assuming 'columns' is a list of column names you want to use
columns = ['number_project', 'overworked', 'last_evaluation', 'tenure']

def load_model(model_path):
    # Use joblib.load to load the model from a joblib file
    model = joblib.load(model_path)
    return model

