import json
import shutil
from flask import Flask, redirect, render_template, send_file, request
import urllib3
from urllib.request import Request, urlopen

## STATIC CONFIG ##

app = Flask(__name__)

global headers
headers = {
    "content-type": "application/json",
    "User-Agent": "nashstore",
    "connection": "close"
}   

## FUNCTIONS ##

def api(url):
    if not url.lower().startswith('http'):
        return str("Not a valid url")
    
    httprequest = Request(url, method="GET", headers=headers)
    with urlopen(httprequest) as response:
        try:
            jsonbody = json.load(response)
        except json.JSONDecodeError:
            jsonbody = ""
    return jsonbody

### WEB KINDA ###

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/applications")
@app.route("/applications/<id>")
def applications(id=None):
    if (id != None):
        j = api("https://store.nashstore.ru/api/mobile/v1/categories/application/" + id)
        return render_template("category.html", j = j)
    
    j = api("https://store.nashstore.ru/api/mobile/v1/categories/application")
    return render_template("app_categories.html", j = j)

@app.route("/games")
@app.route("/games/<id>")
def games(id=None):
    if (id != None):
        j = api("https://store.nashstore.ru/api/mobile/v1/categories/game/" + id)
        return render_template("category.html", j = j)
    
    j = api("https://store.nashstore.ru/api/mobile/v1/categories/game")
    return render_template("game_categories.html", j = j)

@app.route("/app/<id>")
def apk (id=None):
    j = api("https://store.nashstore.ru/api/mobile/v1/application/" + id)
    return render_template("app.html", j = j)

@app.route("/download")
def download():
    url = "https://cdnb.nashstore.ru/store/install/" + request.args.get('url', None)
    name = request.args.get('name', None)
    http = urllib3.PoolManager()
    try:
        return send_file("cache/" + name, as_attachment=True)
    except FileNotFoundError:
        with http.request('GET', url, preload_content=False) as r, open("cache/" + name, 'wb') as out_file:       
            shutil.copyfileobj(r, out_file)
        return send_file("cache/" + name, as_attachment=True)
