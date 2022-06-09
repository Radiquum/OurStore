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
    
def download(url, name):
    http = urllib3.PoolManager()
    try:
        return send_file("cache/" + name, as_attachment=True)
    except FileNotFoundError:
        with http.request('GET', url, preload_content=False) as r, open("cache/" + name, 'wb') as out_file:       
            shutil.copyfileobj(r, out_file)
        return send_file("cache/" + name, as_attachment=True)

### WEB KINDA ###

@app.route("/")
def index():
    return render_template('index.html', page="", title="Главная", description="OurStore - это неофициальный вэб клиент для NashStore, сделанный на Python + Flask")

@app.route("/applications")
@app.route("/applications/<id>")
def applications(id=None):
    if (id != None):
        j = api("https://store.nashstore.ru/api/mobile/v1/categories/application/" + id)
        return render_template("category.html", j = j, page="applications/" + id, title="Приложения > " + j['list'][0].get('category'))
    
    j = api("https://store.nashstore.ru/api/mobile/v1/categories/application")
    return render_template("available_categories.html", j = j, page="applications", title="Приложения")

@app.route("/games")
@app.route("/games/<id>")
def games(id=None):
    if (id != None):
        j = api("https://store.nashstore.ru/api/mobile/v1/categories/game/" + id)
        return render_template("category.html", j = j, page="games/" + id, title="Игры > " + j['list'][0].get('category'))
    
    j = api("https://store.nashstore.ru/api/mobile/v1/categories/game")
    return render_template("available_categories.html", j = j, page="games", title="Игры")

@app.route("/application")
@app.route("/application/<id>")
def apk (id=None):
    if (id == None):
        return redirect("/")
    
    j = api("https://store.nashstore.ru/api/mobile/v1/application/" + id)
    s = json.dumps(j['app']['screens'])
    s = json.loads(s)
    return render_template("application.html", j = j, s=s, page="application/" + id, title=j['app'].get('title'), description=j['app'].get('short_description'), image=j['app'].get('icon') + "/original")

@app.route("/download")
def get_application ():
    try:
        url = "https://cdnb.nashstore.ru/store/install/" + request.args.get('url')
        name = request.args.get('name')
        return download(url, name)
    except TypeError:
        return str('Not a valid download URL')
