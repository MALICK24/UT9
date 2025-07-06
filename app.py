from flask import Flask, render_template, jsonify, abort
import json
import os

app = Flask(__name__)

# Charger les données une seule fois au démarrage
with open('Get1x2_VZip.json', encoding='utf-8') as f:
    data = json.load(f)
    matchs = data.get('Value', [])

def get_match_by_id(match_id):
    for match in matchs:
        if str(match.get('I')) == str(match_id):
            return match
    return None

@app.route('/')
def index():
    # Page principale : liste des matchs
    return render_template('index.html', matchs=matchs)

@app.route('/detail/<match_id>')
def detail(match_id):
    match = get_match_by_id(match_id)
    if not match:
        abort(404)
    return render_template('detail.html', match=match)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 5000))) 
