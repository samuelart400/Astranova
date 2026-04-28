import os
from flask import Flask, jsonify
from supabase import create_client
from dotenv import load_dotenv

# 1. Load configuration
# This automatically looks for a .env file locally
# And Railway automatically maps your "Variables" to environment variables
load_dotenv()

app = Flask(__name__)

# 2. Get environment variables
url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")

# 3. Initialize Supabase
# The if-check ensures we don't crash without keys
if not url or not key:
    print("CRITICAL: Missing SUPABASE_URL or SUPABASE_KEY!")
    supabase = None
else:
    supabase = create_client(url, key)

# 4. Routes
@app.route('/', methods=['GET'])
def home():
    return jsonify({
        "status": "Astranova OS Online", 
        "version": "1.0.0",
        "message": "Transaction Infrastructure Active"
    })

@app.route('/test-db', methods=['GET'])
def test_db():
    if not supabase:
        return jsonify({"status": "Error", "message": "Supabase client not initialized"}), 500
    
    try:
        # Test connection by fetching one record
        data = supabase.table("profiles").select("*").limit(1).execute()
        return jsonify({"status": "Connected to Database!", "data": data.data})
    except Exception as e:
        return jsonify({"status": "Error", "message": str(e)}), 500

if __name__ == '__main__':
    # Railway sets the PORT environment variable
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)