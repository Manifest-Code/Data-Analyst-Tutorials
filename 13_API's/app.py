# import flask
from flask import Flask, jsonify
import requests

API_KEY = "183b66fdc96f4ba5a8d7815f0a48b2f0"

# create instance
app = Flask(__name__)
url = "https://newsapi.org/v2/everything?q=tesla&from=2026-01-25&sortBy=publishedAt&apiKey=183b66fdc96f4ba5a8d7815f0a48b2f0"

#def funct
@app.route("/api/news", methods = ["GET"])   ## give any route name
def get_news():
    response = requests.get(url) 
    if response.status_code == 200: 
        Data = response.json() 
        total_articles = len(Data["articles"])
        first_article = Data["articles"][0]
        author = first_article["author"]
        title = first_article['title']
        published_At = first_article["publishedAt"]

        output_data = {"Total Article Count": total_articles,
               "Title": title,
               "Author": author,
               "Published_At": published_At
               }
        
        return jsonify(output_data)
    else:
        return jsonify({"msg": "Invalid API Key"})
    
# --- ADD THIS BLOCK TO START THE SERVER ---
if __name__ == "__main__":
    print("Flask server is starting...")
    app.run(debug=True, port=5000)    

