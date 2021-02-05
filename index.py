#!/usr/bin/env python
from flask import Flask, render_template, request, session, Response, make_response, redirect, jsonify
import datetime
import sqlite3
import pymysql
import time
import string
import random
application = Flask(__name__)




@application.route('/')
def index():
    return render_template('main.html')


# @application.errorhandler(404)
# def page_not_found(e):
#     return render_template("errors.html") #('404.html')


if __name__=="__main__":
    application.run(host='192.168.3.3', port='8000', debug=True, threaded=True)
