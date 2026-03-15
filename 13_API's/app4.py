from flask import Flask, request, jsonify, render_template
import pandas as pd
import pickle
import os

app = Flask(__name__)

def get_cleaned_data(form_data):
    gestation = float(form_data['gestation'])
    parity = int(form_data['parity'])
    age = float(form_data['age'])
    height = float(form_data['height'])
    weight = float(form_data['weight'])
    smoke = float(form_data['smoke'])

    cleaned_data = {"gestation":[gestation],
                    "parity":[parity],
                    "age":[age],
                    "height":[height],
                    "weight":[weight],
                    "smoke":[smoke]
                    }
    return cleaned_data

@app.route("/", methods = ['GET'])
def home():
    return render_template("index1.html")

@app.route("/hello", methods = ['GET'])
def hello():
    return "Hello World"


# sometimes when we get data from test.py format changes so use a format here
Expected_columns = ["gestation", "parity", "age", "height", "weight", "smoke"]  # this is the order of columns in which we trained our model


@app.route("/predict", methods = ['POST']) 
def get_prediction():
   
    ## baby_data_form = request.form 
    baby_data_form = request.get_json() 

    # baby_data_cleaned = get_cleaned_data(baby_data_form) # because getting json data no need to clean the data

    
    baby_df = pd.DataFrame(baby_data_form)
    baby_df = baby_df[Expected_columns]    # re-ordering the columns in the same order as we trained the model

    # when flask run it will run current directory but it can create a problem for test.py file
    # so we provide a path to it
    path = os.path.join(os.path.dirname(__file__), "model/model.pkl")
    with open(path, 'rb') as obj:
        model = pickle.load(obj)

   
    prediction = model.predict(baby_df)
    prediction = round(float(prediction[0]), 2)

    
    response = {"prediction": prediction}
    # return render_template("index1.html", prediction=prediction)
    return response  # instead render return response   


if __name__ == '__main__':
    app.run(debug=True)