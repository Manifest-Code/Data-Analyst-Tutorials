# create form_1.html file in templates folder
# import flask
from flask import Flask, render_template, request ## flask request not python labrary requests


# create instance
app_1 = Flask(__name__)


#def funct to get (render) html form
@app_1.route('/', methods = ['GET'])
def home():
    return render_template('form_1.html')

#def to show message after user click on submit button
@app_1.route('/upload', methods = ['POST'])
def get_data():
    file = request.files['file']  # files contains all attributes present in files
    #['file'] - file is the name of form we have given in form_1.html
    
    print("This is what it contains", request.files)
    print("file: ", file)

    if file.filename.endswith('.csv'):
        path = 'userfile/' + file.filename #first create a userfile folder in vs code
        file.save(path) 

        ## This creates a string that tells the computer where to put the file. 'userfile/': This is the destination folder (directory).
         ##  file.filename: This is the original name the user gave the file. Result: If a user uploads data.csv, the path becomes userfile/data.csv.
         ## file.save(path): This is the command that actually moves the file from the computer's memory (RAM) onto your hard drive.
        
        return "We have received your file"
    else:
        return "uplaid a CSV file only."
   
    
# --- ADD THIS BLOCK TO START THE SERVER ---
if __name__ == "__main__":
    print("Flask server is starting...")
    app_1.run(debug=True, port=5000)    

