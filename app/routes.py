# app/routes.py
from flask import Blueprint, render_template

app = Blueprint('routes', __name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/exam')
def exam():
    return render_template('exam.html')