# OurStore

(W. I. P.) Unofficial web client for NashStore.ru 

![Last commit](https://img.shields.io/github/last-commit/radiquum/ourstore?style=for-the-badge)
![Deploy](https://img.shields.io/github/workflow/status/radiquum/ourstore/Deploy?label=Deploy&style=for-the-badge)
[![CodeFactor grade](https://img.shields.io/codefactor/grade/github/radiquum/ourstore?style=for-the-badge)](https://www.codefactor.io/repository/github/radiquum/ourstore)
![License](https://img.shields.io/github/license/radiquum/ourstore?style=for-the-badge)
[![Made by Radiquum](https://img.shields.io/badge/Made%20by%20Radiquum-paws.cf-pink?style=for-the-badge)](https://paws.cf)

## Features

- [X] Fetch and display app & game categories
- [X] Downloading applications
- [ ] Search by applications
- [ ] Nice looking UI
- [ ] Bug free

## Local development

1. install python 3.10
2. install requirements.txt
3. download [localhost.direct certificate](http://get.localhost.direct)
4. place localhost.direct.crt and .key to folder with app.py
5. edit your hosts file, to point localhost.direct to 127.0.0.1
6. flask run --cert localhost.direct.crt --key localhost.direct.key --host 127.0.0.1 --port (yourport)
7. you can now access it by typing "https://localhost.direct:(yourport)" in the browser

## Deployment on heroku

1. create a new heroku app
2. click "Use public template"
3. set repository secrets (Settings -> Secrets -> Actions)
4. HEROKU_APP_NAME (name which was used for the new heroku app)
5. HEROKU_API_KEY (can be found in Account Setting)
6. HEROKU_EMAIL (email which you use to register heroku account)
7. re-run deploy action

![Uses HTML](https://forthebadge.com/images/badges/uses-html.svg)
![Uses CSS](https://forthebadge.com/images/badges/uses-css.svg)
![Uses Badges](https://forthebadge.com/images/badges/you-didnt-ask-for-this.svg)
![Made with python](https://forthebadge.com/images/badges/made-with-python.svg)
[![forthebadge](https://forthebadge.com/images/badges/powered-by-black-magic.svg)](https://forthebadge.com)
