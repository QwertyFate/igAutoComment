from flask import Flask, request
from instagrapi import Client
from dotenv import load_dotenv
from instagrapi.exceptions import LoginRequired
from instagrapi.mixins.challenge import ChallengeChoice
import os
import email
import imaplib
import re
import random
import logging



logger = logging.getLogger()
load_dotenv()
cl = Client()   
app = Flask(__name__)
listofsession = {"qwertymake001@gmail.com" : "session.json", "instaqwertygram001@gmail.com" : "session1.json", "dummyinstacomment@gmail.com" : "dummyinstacomment@gmail.com"}


def get_code_from_email(username):
    return "hello"

def challenge_code_handler(username, choice):
    if choice == ChallengeChoice.EMAIL:
        return get_code_from_email(username)
    return False









@app.route("/")
def home():
    print("hello world")
    return("hello world")

@app.route("/registerig", methods=["POST"])
def loginIG():
    data = request.get_json()
    igEmail = data["igEmail"]
    igPW = data["igPW"]
    cl.login(igEmail, igPW)
    cl.dump_settings(f"{igEmail}.json")
    return "successfully created session data"

@app.route("/test", methods=["POST"])
def test():
    cl = Client()
    cl.challenge_code_handler = challenge_code_handler

@app.route("/comment", methods=["POST"])
def comment():
    data = request.get_json()
    cl = Client()
    sessionEmail = data["igEmail"]
    sessionSet = f"{sessionEmail}.json"
    cl.load_settings(f"{sessionSet}")
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




   