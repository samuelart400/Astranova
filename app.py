import secrets # Imports our local secrets.py
from flask import Flask, jsonify
from supabase import create_client

app = Flask(__name__)

# Fetch variables from our local secrets file
url = secrets.SUPABASE_URL
key = secrets.SUPABASE_KEY

# Initialization logic
try:
    supabase = create_client(url, key)
    print("SUCCESS: Supabase client initialized via secrets.py.")
except Exception as e:
    print(f"CRITICAL: Failed to initialize Supabase: {e}")

@app.route('/')
def home():
    return jsonify({"status": "Astranova OS Online", "connection": "Active"})

@app.route('/test-db')
def test_db():
    return jsonify({"status": "Connected to Database!"})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)