from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def show_ip():
    user_ip = request.remote_addr
    return f"<h1>Your IP address is: {user_ip}</h1>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
