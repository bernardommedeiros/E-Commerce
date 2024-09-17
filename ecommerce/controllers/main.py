from flask import render_template
from ecommerce import app

@app.route("/home")
@app.route("/index")
@app.route("/")
def index():
    return render_template('index.html')

@app.route("/feminino_vestuario")
def feminino():
    return render_template('feminino.html')

@app.route("/feminino_tenis")
def feminino_tenis():
    return render_template('tenisFeminino.html')

@app.route("/masculino_vestuario")
def masculino():
    return render_template('masculino.html')

@app.route("/masculino_tenis")
def masculino_tenis():
    return render_template('tenisMasculino.html')