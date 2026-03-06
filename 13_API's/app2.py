from flask import Flask, request, jsonify, render_template
import pandas as pd
import pickle

app = Flask(__name__)

@app.route("/", methods = ['GET'])
def home():
    return render_template("index1.html")


## define your endpoint
@app.route("/predict", methods = ['POST']) # post method because we are sending data to the server
def get_prediction():
    # get data from user
    baby_data = request.get_json()     # get cause user data is sensitve and we dont want to send it in url, we use post method and get_json() to get the data in json format

    # convert into dataframe
    baby_df = pd.DataFrame(baby_data)

    # load machine learning trained model
    with open("model/model.pkl", "rb") as obj:
        model = pickle.load(obj)

    # make prediction on user data
    prediction = model.predict(baby_df)
    prediction = round(float(prediction[0]), 2)

    # return response in a json format
    response = {"prediction": prediction}
    return jsonify(response)



if __name__ == '__main__':
    app.run(debug=True)