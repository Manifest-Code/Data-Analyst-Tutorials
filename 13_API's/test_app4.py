from app4 import app  # app3 is the file we craeted where code is written and app is a flask variable

## first positive test case for "/hello"  route
def test_hello_route_success():
    tester = app.test_client()  # test_client is a method in flask which allows us to test our flask application without running the server (like a dummy browser)
    response = tester.get("/hello")  # get method to send a get request to the server and /hello is the endpoint we want to test

    assert response.status_code == 200 # assert is use to check the condition in testing
    # whenever cond is true it will execute continuously but when its false it will throw assertion error
     

## Failure test case for "/hello" route
"""def test_hello_route_failure():
    tester = app.test_client()  
    response = tester.get("/hello")  

    assert response.status_code == 500
"""

## positive test case for "/predict" route

def test_predict_route_success():
    tester = app.test_client()

    data = {"gestation":[279],
            "parity":[0],
            "age":[27],
            "height":[70],
            "weight":[100],
            "smoke":[0]
            }
    response = tester.post("/predict", json=data)

    assert response.status_code==200


  
# Incorrect data type test case for "/predict" route
def test_predict_route_invalid_data():
    tester = app.test_client()

    data = {"gestation":['279'],  #sending string instead of integer
            "parity":[0],
            "age":[27],
            "height":[70],
            "weight":[100],
            "smoke":[0]
            }
    response = tester.post("/predict", json={})

    assert response.status_code==400   # status code 400 is for bad request when we send incorrect data to the server it will return 400 status code



## Wrong endpoint test case for "/predict" route
def test_predict_route_wrong_url():
    tester = app.test_client()

    data = {"gestation":[279],
            "parity":[0],
            "age":[27],
            "height":[70],
            "weight":[100],
            "smoke":[0]
            }
    response = tester.post("/oredict", json=data)

    assert response.status_code==404   # status code 404 is for not found when we send request to wrong endpoint it will return 404 status code


## Wrong method (get) test case for "/predict" route
def test_predict_route_wrong_method():
    tester = app.test_client()

    data = {"gestation":[279],
            "parity":[0],
            "age":[27],
            "height":[70],
            "weight":[100],
            "smoke":[0]
            }
    response = tester.get("/predict", json=data)

    assert response.status_code==405  # status code 405 is for method not allowed when we send request to correct endpoint but wrong method it will return 405 status code



