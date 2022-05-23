# OurStore
Unofficial web client for NashStore.ru

(W I P)

## Local development

1. install python 3.10
2. install requirements.txt
3. download [localhost.direct certificate](http://get.localhost.direct)
4. place localhost.direct.crt and .key to folder with app.py
5. edit your hosts file, to point localhost.direct to 127.0.0.1
6. set HOST_URL to "https://localhost.direct:[anyport]"
7. flask run app.py --cert localhost.direct.crt --key localhost.direct.key --port [port from 6]