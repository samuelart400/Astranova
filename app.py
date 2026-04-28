import os
from flask import Flask, jsonify
from flask_cors import CORS
from supabase import create_client

app = Flask(__name__)

# This enables cross-origin requests from your future React frontend
CORS(app)

# Railway injects variables directly into the OS environment
url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")

# Initialize Supabase
supabase = create_client(url, key)

@app.route('/')
def home():
    return jsonify({"status": "Astranova OS Online", "cors": "Enabled"})

@app.route('/api/data')
def get_data():
    # Example: How you will fetch from your DB in the future
    # response = supabase.table("your_table").select("*").execute()
    return jsonify({"message": "API is ready for your React frontend"})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)