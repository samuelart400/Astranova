from flask import Flask, jsonify
from supabase import create_client
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")

supabase = create_client(url, key)

# ADD THIS ROUTE FOR THE HOME PAGE
@app.route('/', methods=['GET'])
def home():
    return jsonify({"status": "Astranova OS Online", "version": "1.0.0"})

# KEEP THIS ROUTE FOR THE DATABASE TEST
@app.route('/test-db', methods=['GET'])
def test_db():
    try:
        data = supabase.table("profiles").select("*").limit(1).execute()
        return jsonify({"status": "Connected to Database!", "data": data.data})
    except Exception as e:
        return jsonify({"status": "Error", "error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)