import json
import pymongo
from bson.objectid import ObjectId
import os

from flask import Flask, redirect, url_for, request, render_template, Response, jsonify, session
from werkzeug.utils import secure_filename

from functools import wraps
from http.client import responses
from time import time
import time
from werkzeug.security import generate_password_hash, check_password_hash
from flask_restful import Resource, Api
from flask_httpauth import HTTPTokenAuth
from flask_cors import CORS
from datetime import timedelta


app = Flask(__name__)
api = Api(app)

app.config['PERMANENT_SESSION_LIFETIME'] =  timedelta(minutes=120)



#------------------------------------DATABASE------------------------------------#
try:
    # mongo = pymongo.MongoClient(
    #     host="localhost",
    #     port=27017,
    #     serverSelectionTimeoutMS=1000
    # )
    # db = mongo.ndonga
    mongo = pymongo.MongoClient("mongodb+srv://syaefudinfikri:gtQC4zcxAycDBOCc@ndonga.rjdxc7m.mongodb.net/")
    db = mongo.ndonga
    mongo.server_info()
except:
    print("ERROR Connect To Database")

@app.route("/")
def index():
    return "welcome"

@app.route("/api")
def apii():
    data = db['belajar'].find()
    datajson = []
    for i in data:
        jsonn = {"nama":i['nama'],"isi":i['isi']}
        datajson.append(jsonn)
    print(datajson)
    return jsonify({"data":datajson}),200

CORS(app)

#development
if __name__ == "__main__":
    app.run(host="0.0.0.0",port=8000,debug=True)