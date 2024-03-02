from flask import Flask, render_template, request
import requests
import os 

app = Flask(__name__)

# GitHub API base URL
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
API_BASE_URL = 'https://api.github.com/search/users'

# Your GitHub access token
ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN")


@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        location = request.form['location']
        headers = {'Authorization': f'Bearer {ACCESS_TOKEN}'}
        query = f'location:{location}'
        params = {'q': query, 'per_page': 100} 
        response = requests.get(API_BASE_URL, params=params, headers=headers)
        if response.status_code == 200:
           data = response.json()
           users = data.get('items', [])
           return render_template('index.html', users=users)
        else:
           return "Error: Unable to fetch users"
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

