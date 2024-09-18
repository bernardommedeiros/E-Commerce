from flask import render_template, flash
from flask_login import login_user
from ecommerce import app, db

from ecommerce.models.tables import Usuario
from ecommerce.models.forms import LoginForm

@app.route("/home", methods=["GET", "POST"])
@app.route("/index", methods=["GET", "POST"])
@app.route("/", methods=["GET", "POST"])
def index():
    loginform = LoginForm()
    if(loginform.validate_on_submit()):
        cursor = db.cursor()
        usuarioDB = cursor.execute("SELECT * FROM users WHERE usuario =%s and senha =%s", (loginform.usuario.data, loginform.senha.data))
        if(usuarioDB > 0):
            cursorIdEmail = db.cursor()
            cursorIdEmail.execute("SELECT id, email FROM users WHERE usuario=%s and senha=%s", (loginform.usuario.data, loginform.senha.data))
            login_user(Usuario.instanciar(cursorIdEmail.fetchone(), loginform.usuario.data, cursorIdEmail.fetchone(), loginform.senha.data))
            flash("Logado!")
        else:
            flash("Valores inválidos!")
    return render_template('index.html', login_form=loginform)

@app.route("/feminino_vestuario", methods=["GET", "POST"])
def feminino():
    loginform = LoginForm()
    return render_template('feminino.html', login_form=loginform)

@app.route("/feminino_tenis", methods=["GET", "POST"])
def feminino_tenis():
    loginform = LoginForm()
    return render_template('tenisFeminino.html', login_form=loginform)

@app.route("/feminino_acessorios", methods=["GET", "POST"])
def feminino_acessorios():
    loginform = LoginForm()
    return render_template('acessoriosFeminino.html', login_form=loginform)

@app.route("/masculino_vestuario", methods=["GET", "POST"])
def masculino():
    loginform = LoginForm()
    return render_template('masculino.html', login_form=loginform)

@app.route("/masculino_tenis", methods=["GET", "POST"])
def masculino_tenis():
    loginform = LoginForm()
    return render_template('tenisMasculino.html', login_form=loginform)

@app.route("/masculino_acessorios", methods=["GET", "POST"])
def masculino_acessorios():
    loginform = LoginForm()
    return render_template('acessoriosMasculino.html', login_form=loginform)