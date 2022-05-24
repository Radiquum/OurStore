from flask import Flask, redirect, render_template, send_file, request

import requests
import http.client
import json
import os

import urllib.request


## STATIC CONFIG ##

app = Flask(__name__)

global URL
URL = "store.nashstore.ru"

global headers
headers = {
            "content-type": "application/json",
            "user-agent": "Nashstore",
            "Connection": "keep-alive"
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

@app.route("/api/game_categories")
def api_game_categories():
    connection.request("GET", "/api/mobile/v1/categories/game", headers=headers)
    responce = connection.getresponse()
    msg = json.loads(responce.read().decode())
    return msg

@app.route("/api/category/<id>")
def api_category(id=None):
    connection.request("GET", "/api/mobile/v1/categories/application/" + id, headers=headers)
    responce = connection.getresponse()
    msg = json.loads(responce.read().decode())
    return msg

@app.route("/api/game_category/<id>")
def api_game_category(id=None):
    connection.request("GET", "/api/mobile/v1/categories/game/" + id, headers=headers)
    responce = connection.getresponse()
    msg = json.loads(responce.read().decode())
    return msg

@app.route("/api/app/<id>")
def api_app(id=None):
    connection.request("GET", "/api/mobile/v1/application/" + id, headers=headers)
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

@app.route("/games")
def game_categories():
    r = requests.get(HOST_URL + "/api/game_categories")
    j = r.json()    
    return render_template("game_categories.html", j = j)
    
@app.route("/game_category/<id>")
def game_category(id=None):
    r = requests.get(HOST_URL + "/api/game_category/" + id)
    j = r.json()    
    return render_template("category.html", j = j)

@app.route("/app/<id>")
def apk (id=None):
    r = requests.get(HOST_URL + "/api/app/" + id)
    j = r.json()    
    return render_template("app.html", j = j)

@app.route("/download")
@app.route("/download?url=<id>&?name=<str>")
def download():
    url  = request.args.get('url', None)
    name  = request.args.get('name', None)
    
    try:
        return send_file("cache/" + name, as_attachment=True)
    except:
        r = requests.get("https://cdnb.nashstore.ru/store/install/" + url, allow_redirects=True)
        with open("cache/" + name, 'wb') as f:
            f.write(r.content)
        return send_file("cache/" + name, as_attachment=True)


