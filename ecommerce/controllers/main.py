from flask import render_template
from ecommerce import app

@app.route("/home")
@app.route("/index")
@app.route("/")
def index():
    return render_template('index.html')

@app.route("/feminino")
def feminino():
    return render_template('feminino.html')

@app.route("/masculino")
def masculino():
    return render_template('masculino.html')