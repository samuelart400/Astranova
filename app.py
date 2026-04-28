import os
from flask import Flask, jsonify
from supabase import create_client

app = Flask(__name__)

# Railway injects variables directly into the OS environment
url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")

# Initialization
supabase = create_client(url, key)

@app.route('/')
def home():
    return jsonify({"status": "Astranova OS Online"})

@app.route('/test-db')
def test_db():
    return jsonify({"status": "Connected to Database!"})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)