from flask import Flask
from routes import predict, user
from extentions import cache



app = Flask(__name__)

# configure my cache
app.config['CACHE_TYPE'] = 'SimpleCache'


# init cache
cache.init_app(app)



## import your blueprints here and register
app.register_blueprint(user.user_bp) 
app.register_blueprint(predict.predict_bp)


if __name__ == '__main__':
    app.run(debug=True)


## this is your main flask app






























# def get_cleaned_data(form_data):
#     gestation = float(form_data['gestation'])
#     parity = int(form_data['parity'])
#     age = float(form_data['age'])
#     height = float(form_data['height'])
#     weight = float(form_data['weight'])
#     smoke = float(form_data['smoke'])

#     cleaned_data = {"gestation":[gestation],
#                     "parity":[parity],
#                     "age":[age],
#                     "height":[height],
#                     "weight":[weight],
#                     "smoke":[smoke]
#                     }

#     return cleaned_data







# EXCPECTED_COLUMNS = ["gestation","parity","age","height","weight","smoke"]

# define your endpoint
# @app.route("/predict", methods = ['POST'])
# def get_prediction():
#     # get data from user
#     # baby_data_form = request.form
#     baby_data_form = request.get_json()


#     # baby_data_cleaned = get_cleaned_data(baby_data_form)

#     # convert into dataframe
#     baby_df = pd.DataFrame(baby_data_form)
#     baby_df = baby_df[EXCPECTED_COLUMNS]

#     # load machine leanring trained model
#     path = os.path.join(os.path.dirname(__file__), "model.pkl")
#     with open(path, 'rb') as obj:
#         model = pickle.load(obj)

#     # make prediciton on user data
#     prediction = model.predict(baby_df)
#     prediction = round(float(prediction), 2)

#     # return reponse in a json format
#     response = {"Prediction":prediction}

#     # return render_template("index.html", prediction=prediction)
#     return response





# ROUTES FOR USER

# @app.route('/get-user', methods=['GET'])
# def get_user():
#     return "This is Get user route."

# @app.route('/get-user', methods=['PUT'])
# def update_user():
#     return "This is Update user route." 

# @app.route('/get-user', methods=['POST'])
# def create_user():
#     return "This is Create user route."

# @app.route('/get-user', methods=['DELETE'])
# def delete_user():
#     return "This is Delete user route."





