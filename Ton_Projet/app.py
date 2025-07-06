from flask import Flask, render_template, abort
import requests
import os

app = Flask(__name__)

API_URL = "https://1xbet.com/LiveFeed/Get1x2_VZip?sports=85&count=50&lng=fr&gr=70&mode=4&country=96&getEmpty=true"

def fetch_matchs():
    response = requests.get(API_URL)
    data = response.json()
    return data.get('Value', [])

def get_match_by_id(match_id, matchs):
    for match in matchs:
        if str(match.get('I')) == str(match_id):
            return match
    return None

@app.route('/')
def index():
    matchs = fetch_matchs()
    return render_template('index.html', matchs=matchs)

@app.route('/detail/<match_id>')
def detail(match_id):
    matchs = fetch_matchs()
    match = get_match_by_id(match_id, matchs)
    if not match:
        abort(404)
    return render_template('detail.html', match=match)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 5000))) 
