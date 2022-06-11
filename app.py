import json
import shutil
from urllib.error import HTTPError
from flask import Flask, redirect, render_template, send_file, request, abort
import urllib3
from urllib.request import Request, urlopen

app = Flask(__name__)

## FUNCTIONS ##


def api(url):
    if not url.lower().startswith('http'):
        return str("Not a valid url")

    headers = {
        "content-type": "application/json",
        "User-Agent": "nashstore",
        "connection": "close"
    }

    try:
        httprequest = Request(url, method="GET", headers=headers)
        with urlopen(httprequest) as response:
            jsonbody = json.load(response)
    except json.JSONDecodeError:
        abort(404)
    except HTTPError:
        abort(400)

    return jsonbody


def download(url, name):
    http = urllib3.PoolManager()
    try:
        return send_file(f"cache/{name}", as_attachment=True)
    except FileNotFoundError:
        with http.request('GET', url, preload_content=False) as r, open(f"cache/{name}", 'wb') as out_file:
            shutil.copyfileobj(r, out_file)
        return send_file(f"cache/{name}", as_attachment=True)

### WEB KINDA ###


@app.route("/")
def index():
    page = {
        "page": "",
        "title": "Главная",
        "description": "OurStore - это неофициальный вэб клиент для NashStore, сделанный на Python + Flask"
    }
    return render_template('index.html', page=page)


@app.route("/applications")
@app.route("/applications/<id>")
def applications(id=None):

    if (id is not None):
        j = api(
            f"https://store.nashstore.ru/api/mobile/v1/categories/application/{id}")
        page = {
            "page": f"applications/{id}",
            "title": f"Приложения > {j['list'][0].get('category')}",
        }
        return render_template("category.html", j=j, page=page)

    page = {
        "page": "applications",
        "title": "Приложения",
    }

    j = api("https://store.nashstore.ru/api/mobile/v1/categories/application")
    return render_template("available_categories.html", j=j, page=page)


@app.route("/games")
@app.route("/games/<id>")
def games(id=None):
    if (id is not None):
        j = api("https://store.nashstore.ru/api/mobile/v1/categories/game/" + id)
        page = {
            "page": f"applications/{id}",
            "title": f"Игры > {j['list'][0].get('category')}",
        }
        return render_template("category.html", j=j, page=page)

    page = {
        "page": "games",
        "title": "Игры",
    }

    j = api("https://store.nashstore.ru/api/mobile/v1/categories/game")
    return render_template("available_categories.html", j=j, page=page)


@app.route("/application")
@app.route("/application/<id>")
def apk(id=None):
    if (id is None):
        return redirect("/")

    j = api(f"https://store.nashstore.ru/api/mobile/v1/application/{id}")
    page = {
        "page": f"application/{id}",
        "title": j['app'].get('title'),
        "description": j['app'].get('short_description'),
        "image": f"{j['app'].get('icon')}/original"
    }
    s = j['app']['screens']
    return render_template("application.html", j=j, s=s, page=page)


@app.route("/download")
def get_application():
    try:
        url = f"https://cdnb.nashstore.ru/store/install/{request.args.get('url')}"
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
    return render_template('error.html', code="404", description="Not Found"), 404


@app.errorhandler(500)
def server_error(e):
    return render_template('error.html', code="500", description="Internal Server Error"), 500


if __name__ == "__main__":
    app.run()
