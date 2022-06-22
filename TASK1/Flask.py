from flask import Flask, jsonify, request, render_template
import json
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello Flask!"

@app.route('/pincode')
def pincode():
    return render_template('Test.html')

@app.route('/create_file', methods=['POST'])
def create_file():
    if request.method == 'POST':
        pinc=json.loads(request.data)
        newurl="https://api.postalpincode.in/pincode/" + pinc["pin"]
        x = requests.get(newurl)
        return x.json()[0]
       
if __name__ == "__main__":
    app.run(debug=True)
