import streamlit as st
import numpy as np
import pandas as pd
import joblib
from utils import load_model

# Load the model using pickle
model_path = 'https://github.com/databulance/Employee_Churn_ML/blob/main/hr_rf2.joblib'
model = load_model(model_path)

st.title("Predicting if an employee will stay or leave Salifort")
# last_evaluation score
last_evaluation = st.slider("Evaluation Score", 0.0, 1.0)
# number of project
number_project = st.slider("Number of project(s)", 0, 20)
# tenure (number of years working at the company)
tenure = st.slider("Tenure", 0, 30)
# work accident
work_accident = st.selectbox("Number of Accident(s)", [0, 1])
# promotion last 5 years
promotion_last_5years = st.selectbox("Promoted last 5 years", [0, 1])
# Salary
salary_options = ["Low", "Medium", "High"]
salary = st.select_slider("Salary level", salary_options)
# Overworked
overworked = st.slider("Hours worked", 96, 310)

# Department
department_options = ["IT", "RandD", "Accounting", "HR", "Management", "Marketing", "Product Mng", "Sales", "Support", "Technical"]
selected_department = st.multiselect("Department", department_options)

# Convert selected department to Boolean values
department_values = [True if department in selected_department else False for department in department_options]

# Create DataFrame for prediction
data = {
    "last_evaluation": last_evaluation,
    "number_project": number_project,
    "tenure": tenure,
    "work_accident": work_accident,
    "promotion_last_5years": promotion_last_5years,
    "department_IT": department_values[0],
    "department_RandD": department_values[1],
    "department_accounting": department_values[2],
    "department_hr": department_values[3],
    "department_management": department_values[4],
    "department_marketing": department_values[5],
    "department_product_mng": department_values[6],
    "department_sales": department_values[7],
    "department_support": department_values[8],
    "department_technical": department_values[9],
    "salary_high": salary == "High",
    "salary_low": salary == "Low",
    "salary_medium": salary == "Medium",
    "overworked": overworked
}

x = pd.DataFrame([data])

def predict():
    prediction = model.predict(x)
    if prediction[0] == 0:
        st.success("Employee is likely to stay.")
    else:
        st.error("Employee is likely to leave.")

trigger = st.button("Predict", on_click=predict)
