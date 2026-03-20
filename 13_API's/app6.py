from flask import Flask, request
from routes import predict, user


app = Flask(__name__)


## import your blueprints here and register
app.register_blueprint(user.user_bp) 
app.register_blueprint(predict.predict_bp)


if __name__ == '__main__':
    app.run(debug=True)


## this is your main flask app