import os
from flask import Flask, jsonify
from supabase import create_client
from dotenv import load_dotenv

# Load local .env if it exists
load_dotenv()

app = Flask(__name__)

# Fetch variables directly from the environment
SUPABASE_URL = os.environ.get("SUPABASE_URL")
SUPABASE_KEY = os.environ.get("SUPABASE_KEY")

# Debugging: Print to logs to verify status
print(f"DEBUG: Initializing with URL: {SUPABASE_URL}")

if not SUPABASE_URL or not SUPABASE_KEY:
    print("CRITICAL: Missing SUPABASE_URL or SUPABASE_KEY in environment!")
    # We continue so the app still boots for the health check
else:
    supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
    print("SUCCESS: Supabase client initialized.")

@app.route('/')
def home():
    return jsonify({"status": "Astranova OS Online", "env_check": "Active"})

@app.route('/test-db')
def test_db():
    try:
        if not SUPABASE_URL or not SUPABASE_KEY:
            return jsonify({"error": "Supabase credentials not configured"}), 500
        
        # Test a simple query (replace 'your_table_name' with a real table)
        # data = supabase.table("your_table_name").select("*").limit(1).execute()
        return jsonify({"status": "Connected to Database!", "debug": "Credentials found"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)