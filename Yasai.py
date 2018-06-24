from flask import Flask, render_template, request
from json import *

import YasaiDb
from Camera import take_image

app = Flask(__name__)

@app.route('/')
def index():
    items = YasaiDb.query_latest_images(20)
    return render_template('index.html', title="Top", items=items)

@app.route('/now')
def now():
    return render_latest(title="Now")

@app.route('/update')
def update():
    return trigger()

def render_latest(title):
    id, name, path = YasaiDb.query_latest_image()
    return render_template('now.html', title=title, img=path)

@app.route('/hello')
def hello():
    name = "Hello world"
    return name

@app.route('/api/trigger')
def trigger():
    ret, path, timestamp = take_image()
    if ret == True:
        ret, id = YasaiDb.insert_photo(path, timestamp)

    if request.method == 'POST':
        dict = {
            "id" : id,
            "result": ret,
            "path": path
        }
        json = dumps(dict)
        return json
    else:
        ret, path, timestamp = take_image()
        title = "Trigger {}".format(path)
        return render_template('now.html', title=title, img=path)


if __name__ == "__main__":
    # app.run(debug=True)
    app.run(debug=False, host='192.168.0.200', port=5000)