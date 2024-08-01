from flask import Flask, render_template, url_for,request
import pickle as p
import pickle
from flask import Flask,request,jsonify,render_template
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler



modelfile = 'models/final_prediction.pickle'  
model = p.load(open(modelfile, 'rb'))
scaler= pickle.load(open('models/scaler.pickle','rb'))
app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index.html') 

@app.route('/predict',methods =['GET','POST'])
def predict():
    gender = float(request.form["gender"])
    age =float(request.form['age'])
    hypertension = float(request.form['hypertension'])
    heart_disease=float(request.form['heart_disease'])
    ever_married = float(request.form['ever_married'])
    work_type  = float(request.form['work_type'])
    Residence_type= float(request.form['Residence_type'])
    avg_glucose_level= float(request.form['avg_glucose_level'])
    bmi= float(request.form['bmi'])
    smoking_status= float(request.form['smoking_status'])



    total = [[gender,age,hypertension,heart_disease,ever_married,work_type,Residence_type,
              avg_glucose_level,bmi,smoking_status]]
    prediction = model.predict(scaler.transform(total))
    prediction = int(prediction[0])

    if prediction==0:
        return render_template('index.html',predict="not stroke")
    
    else:
        return render_template('index.html',predict="stroke")       




if __name__ == '__main__':
    app.run(debug=True)
