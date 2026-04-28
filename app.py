import config_secrets  # Ensure this matches your renamed file
from flask import Flask, jsonify
from supabase import create_client
import os

app = Flask(__name__)

# Fetch variables from our local config_secrets.py
url = config_secrets.SUPABASE_URL
key = config_secrets.SUPABASE_KEY

# Initialization logic
try:
    supabase = create_client(url, key)
    print("SUCCESS: Supabase client initialized via config_secrets.py.")
except Exception as e:
    print(f"CRITICAL: Failed to initialize Supabase: {e}")

@app.route('/')
def home():
    return jsonify({
        "status": "Astranova OS Online", 
        "connection": "Active"
    })

@app.route('/test-db')
def test_db():
    return jsonify({"status": "Connected to Database!"})

if __name__ == '__main__':
    # Use the port assigned by Railway or default to 8080
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)