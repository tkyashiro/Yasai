from flask import Flask, render_template, request
from json import *

import YasaiDb
from Camera import take_image

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', title="Top")

@app.route('/now')
def now():
    return render_template('now.html', title="Now")

@app.route('/update')
def update():
    return render_template('now.html', title="update")

@app.route('/hello')
def hello():
    name = "Hello world"
    return name

@app.route('/api/trigger')
def trigger():
    ret, path, timestamp = take_image()
    if ret == True:
        YasaiDb.insert_photo(path, timestamp)

    if request.method == 'POST':
        dict = {
            "result": ret,
            "path": path
        }
        json = dumps(dict)
        return json
    else:
        ret, path, timestamp = take_image()
        title = "Trigger {} {}".format(ret, path)
        return render_template('now.html', title=title, img=path)

if __name__ == "__main__":
    # app.run(debug=True)
    app.run(debug=False, host='192.168.0.200', port=5000)