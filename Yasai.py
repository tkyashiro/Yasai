from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html',
                           name="Index", title="Top")

@app.route('/hello')
def hello():
    name = "Hello world"
    return name

@app.route('/api/trigger')
def trigger():
    return ""

if __name__ == "__main__":
    app.run(debug=True)