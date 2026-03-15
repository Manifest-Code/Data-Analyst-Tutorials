from flask import Flask, request, jsonify

app = Flask(__name__)

## API Key
API_KEY = "myapikey"

# middleware to verify API-Key
def require_api_key(func):
    def wrapper(*args, **kwargs):
        key = request.headers.get('x-api-key')

        if key and key == API_KEY:
            return func(*args, **kwargs)
        else:
            return jsonify({"Error":"Unauthorized, Missing API key"})
    return wrapper    

@app.route("/", methods=["GET"])
def login():
    return "Login Here"

@app.route("/profile", methods=["GET"])
@require_api_key   # middleware/gaurd
def profile():
    return "Profile Page"

if __name__ == "__main__":
    app.run(debug=True)