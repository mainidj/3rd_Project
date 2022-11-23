from flask import Flask, render_template

App = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return 'About 페이지'