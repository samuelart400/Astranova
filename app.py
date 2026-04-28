import os
from flask import Flask, jsonify
from supabase import create_client

app = Flask(__name__)

url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")
supabase = create_client(url, key)

@app.route('/')
def home():
    return jsonify({"status": "Astranova OS Online"})

@app.route('/debug-db')
def debug_db():
    try:
        # Replace 'your_table_name' with an actual table in your Supabase DB
        # If you don't know a table name, use 'auth.users' which exists by default
        response = supabase.table("auth.users").select("id").limit(1).execute()
        return jsonify({"status": "Success", "data_sample": response.data})
    except Exception as e:
        return jsonify({"status": "Error", "message": str(e)})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)