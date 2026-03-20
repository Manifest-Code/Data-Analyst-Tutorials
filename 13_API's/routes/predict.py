import os
import pandas as pd
import pickle
from flask import Blueprint, request
from extentions import cache

PARENT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
path = os.path.join(PARENT_DIR, "model.pkl")

# 2. Load the model globally (happens only once when app starts)
with open(path, 'rb') as obj:
    model = pickle.load(obj)

predict_bp = Blueprint("predict",__name__)




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







EXCPECTED_COLUMNS = ["gestation","parity","age","height","weight","smoke"]





# define your endpoint

@predict_bp.route("/predict", methods = ['POST'])
@cache.cached(timeout=30, query_string=True)
def get_prediction():
    # get data from user
    # baby_data_form = request.form
    baby_data_form = request.get_json()


    # baby_data_cleaned = get_cleaned_data(baby_data_form)

    # convert into dataframe
    baby_df = pd.DataFrame(baby_data_form)
    baby_df = baby_df[EXCPECTED_COLUMNS]

    # load machine leanring trained model
    # path = os.path.join(os.path.dirname(__file__), "model.pkl")
    # path = "C:\\Users\\ASUS VIVOBOOK 14\\Desktop\\Machine Learningh Model\\model.pkl"
    # with open(path, 'rb') as obj:
    #     model = pickle.load(obj)

    # make prediciton on user data
    prediction = model.predict(baby_df)
    result = round(float(prediction[0]), 2)

    # return reponse in a json format
    response = {"Prediction": result}

    # return render_template("index.html", prediction=prediction)
    return response



# 9 sec for first reqeust

"""
query_string=True: This is a crucial security and functional setting.

If False: /search?term=apple and /search?term=banana would be treated as the exact same request. The second person would accidentally see the results for "apple."

If True: The cache creates a unique key based on the URL plus the query parameters. This ensures users get the specific data they actually asked for.

"""
