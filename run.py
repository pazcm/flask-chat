import os # we'll have access to the environment variables
from flask import Flask

app = Flask(__name__) # initialize Flask app

# create app route decorator
@app.route("/")
def index():
    """Main page with instructions"""
    return "To send a message use: /USERNAME/MESSAGE"

@app.route("/<username>")
def user(username):
    return "Hi " + username

@app.route("/<username>/<message>")
def send_message(username, message):
    return "{0}: {1}".format(username, message)
    
# app.run
app.run(host=os.getenv("IP"), port=int(os.getenv("PORT")), debug=True)