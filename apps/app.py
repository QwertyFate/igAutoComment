from flask import Flask, request
from instagrapi import Client
from dotenv import load_dotenv
from instagrapi.exceptions import LoginRequired
import os
import logging

logger = logging.getLogger()
load_dotenv()
igEmail = os.getenv("EMAIL1")
igPW = os.getenv("PASSWORD1")
cl = Client()   
app = Flask(__name__)
listofsession = {"qwertymake001@gmail.com" : "session.json", "instaqwertygram001@gmail.com" : "session1.json"}

@app.route("/")
def home():
    print("hello world")
    return("hello world")

@app.route("/registerig", methods=["POST"])
def loginIG():
    cl.login(igEmail, igPW)
    cl.dump_settings(f"session.json")
    return "successfully created session data"

@app.route("/comment", methods=["POST"])
def comment():
    data = request.get_json()
    cl = Client()
    cl.load_settings(listofsession[data["igEmail"]])
    cl.login (data["igEmail"], data["igPW"]) # this doesn't actually login using username/password but uses the session
    cl.get_timeline_feed()
    media_id = cl.media_id(cl.media_pk_from_url(data["instagramURL"]))
    comment = cl.media_comment(media_id, data["comment"])
    return "commented successfully"

@app.route("/", methods=["POST"])
def hello_world():
    data = request.get_json()
    print(data["igEmail"])
    return listofsession[data["igEmail"]]




   