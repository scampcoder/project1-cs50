import os

from flask import Flask, session, render_template, request
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)

# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set up database
# object from sqlalchemy that manages connection to our db
engine = create_engine(os.getenv("DATABASE_URL"))

# scoped session makes it so that users actions with db are separated
db = scoped_session(sessionmaker(bind=engine))

# main page
@app.route("/")
def index():
    return render_template("index.html")
