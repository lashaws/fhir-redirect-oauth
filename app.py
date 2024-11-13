from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the OAuth Redirect Service!"

@app.route('/callback')
def callback():
    code = request.args.get('code')
    if not code:
        return "Error: No authorization code provided."
    # Process the authorization code here if needed
    return "Authorization successful. You can close this page."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
