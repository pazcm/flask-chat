import os # we'll have access to the environment variables
from flask import Flask, redirect

app = Flask(__name__) # initialize Flask app
messages = [] # create an empty list

def add_messages(username, message):
    """ It takes our user name and message and append it to the `messages` list """
    messages.append("{}: {}".format(username, message))
    
def get_all_messages():
    """Get all of the messages and separate them with a `br`"""
    return "<br>".join(messages)

# create app route decorator
@app.route("/")
def index():
    """ Main page with instructions """
    return "To send a message use: /USERNAME/MESSAGE"

@app.route("/<username>")
def user(username):
    """ Display chat messages """
    return "Welcome {0} - {1}".format(username, get_all_messages())

@app.route("/<username>/<message>")
def send_message(username, message):
    """ Create a new message and redirect back to the chat page"""
    add_messages(username, message) # call new function
    return redirect(username)
    
# app.run
app.run(host=os.getenv("IP"), port=int(os.getenv("PORT")), debug=True)