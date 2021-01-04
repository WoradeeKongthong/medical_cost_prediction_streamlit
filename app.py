from flask import Flask, request
import numpy as np
import pickle
import pandas as pd
import streamlit as st

pickle_in = open("model/MedicalCostRandomForest.pkl","rb")
data=pickle.load(pickle_in)
estimator=data['model']

#@app.route('/')
def welcome():
    return "Welcome to Medical Cost Prediction Project"

#@app.route('/predict', methods=["Get"])
def predict_from_get(age,sex,bmi,children,smoker,region):
  
    x=[age,sex,bmi,children,smoker,region]
    
    # convert x to DataFrame
    col = ['age','sex','bmi','children','smoker','region']
    x = pd.DataFrame(data=[x],columns=col)
    
    prediction=estimator.predict(x)
    
    return "The answer is"+str(prediction)
    # try http://0.0.0.0:8000/predict

def main():
    st.title("medical cost prediction")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Medical Cost Prediction ML App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    age = st.text_input("age","Type Here")
    sex = st.text_input("sex","Type Here")
    bmi = st.text_input("bmi","Type Here")
    children = st.text_input("children","Type Here")
    smoker = st.text_input("smoker","Type Here")
    region = st.text_input("region","Type Here")
    result=""
    if st.button("Predict"):
        result=predict_from_get(age,sex,bmi,children,smoker,region)
        st.success("The output is {}".format(result))
    
if __name__=='__main__':
    main()
    
    
