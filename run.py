import os # we'll have access to the environment variables
from flask import Flask

app = Flask(__name__) # initialize Flask app

# create app route decorator
@app.route("/")
def index():
    return"<h1>Hello There!</h1>"

# app.run
app.run(host=os.getenv("IP"), port=int(os.getenv("PORT")), debug=True)