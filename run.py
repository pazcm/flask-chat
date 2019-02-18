import os # we'll have access to the environment variables
from flask import Flask

app = Flask(__name__) # initialize Flask app
messages = [] # create an empty list

def add_messages(username, message):
    """ It takes our user name and message and append it to the list """
    messages.append("{}: {}".format(username, message))

# create app route decorator
@app.route("/")
def index():
    """ Main page with instructions """
    return "To send a message use: /USERNAME/MESSAGE"

@app.route("/<username>")
def user(username):
    """ Display chat messages """
    return "Welcome {0}".format(username, messages)

@app.route("/<username>/<message>")
def send_message(username, message):
    """ Create a new message and redirect back to the chat page"""
    return "{0}: {1}".format(username, message)
    
# app.run
app.run(host=os.getenv("IP"), port=int(os.getenv("PORT")), debug=True)