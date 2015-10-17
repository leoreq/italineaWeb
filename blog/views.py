from flask import *
from blog import app
from .database import session
#from .models import Post

@app.route("/")
def home():
    return render_template("home.html")
