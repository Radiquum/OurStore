import json
import shutil
from urllib.error import HTTPError
from flask import Flask, redirect, render_template, send_file, request, abort
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
    
    try:
        httprequest = Request(url, method="GET", headers=headers)
        with urlopen(httprequest) as response:
            jsonbody = json.load(response)
    except json.JSONDecodeError:
        abort(404, description="Resource not found")
    except HTTPError:
        abort(400, description="Bad request")
            
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
    
### SOME ERROR HANDLING ###

@app.errorhandler(400)
def bad_request(e):
    return render_template('error.html', code="400", description="Bad Request"), 400

@app.errorhandler(403)
def forbidden(e):
    return render_template('error.html', code="403", description="Forbidden"), 403

@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status, this is what it catches
    return render_template('error.html', code="404", description="Not Found"), 404 

@app.errorhandler(500)
def server_error(e):
    return render_template('error.html', code="500", description="Internal Server Error"), 500
