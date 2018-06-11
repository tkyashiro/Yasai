from flask import Flask, render_template, request

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
    return ""

if __name__ == "__main__":
    # app.run(debug=True)
    app.run(debug=False, host='192.168.0.200', port=5000)