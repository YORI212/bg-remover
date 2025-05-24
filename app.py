from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "✅ It works!"

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    print(f"Starting on port {port}...")
    app.run(host='0.0.0.0', port=port)
