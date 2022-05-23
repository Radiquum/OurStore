from flask import Flask, render_template

import requests
import http.client
import json
import os



## STATIC CONFIG ##

app = Flask(__name__)

global URL
URL = "store.nashstore.ru"

global headers
headers = {
            "content-type": "application/json",
            "user-agent": "Nashstore",
        } 

global connection
connection = http.client.HTTPSConnection(URL)

## REQUIRED CONFIG ##

global HOST_URL
HOST_URL = os.environ.get('HOST_URL')

## API KINDA ###

@app.route("/api/version")
def version():
    connection.request("GET", "/api/v1/nashstore/version", headers=headers)
    responce = connection.getresponse()
    msg = json.loads(responce.read().decode())
    return msg

@app.route("/api/categories")
def api_categories():
    connection.request("GET", "/api/mobile/v1/categories/application", headers=headers)
    responce = connection.getresponse()
    msg = json.loads(responce.read().decode())
    return msg

@app.route("/api/category/<id>")
def api_category(id=None):
    connection.request("GET", "/api/mobile/v1/categories/application/" + id, headers=headers)
    responce = connection.getresponse()
    msg = json.loads(responce.read().decode())
    return msg

### WEB KINDA ###

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/categories")
def categories():
    r = requests.get(HOST_URL + "/api/categories")
    j = r.json()    
    return render_template("categories.html", j = j)
    
@app.route("/category/<id>")
def category(id=None):
    r = requests.get(HOST_URL + "/api/category/" + id)
    j = r.json()    
    return render_template("category.html", j = j)


