from flask import render_template, flash
from flask_login import login_user
from ecommerce import app, db

from ecommerce.models.tables import Usuario
from ecommerce.models.forms import LoginForm

@app.route("/home")
@app.route("/index")
@app.route("/")
def index():
    loginform = LoginForm()
    if(loginform.validate_on_submit()):
        cursor = db.cursor()
        usuarioDB = cursor.execute("SELECT * FROM users WHERE usuario=%s and senha = %s", (loginform.usuario.data, loginform.senha.data))
        if(usuarioDB > 0):
            login_user(Usuario.instanciar(cursor.fetchone("SELECT id FROM users WHERE usuario=%s and senha=%s", (loginform.usuario.data, loginform.senha.data)), loginform.usuario.data, cursor.fetchone("SELECT email FROM users WHERE usuario=%s and senha=%s", (loginform.usuario.data, loginform.senha.data)), loginform.senha.data))
            flash("Logado!")
        else:
            flash("Valores inválidos!")
    return render_template('index.html', login_form=loginform)

@app.route("/feminino_vestuario")
def feminino():
    loginform = LoginForm()
    return render_template('feminino.html', login_form=loginform)

@app.route("/feminino_tenis")
def feminino_tenis():
    loginform = LoginForm()
    return render_template('tenisFeminino.html', login_form=loginform)

@app.route("/feminino_acessorios")
def feminino_acessorios():
    loginform = LoginForm()
    return render_template('acessoriosFeminino.html', login_form=loginform)

@app.route("/masculino_vestuario")
def masculino():
    loginform = LoginForm()
    return render_template('masculino.html', login_form=loginform)

@app.route("/masculino_tenis")
def masculino_tenis():
    loginform = LoginForm()
    return render_template('tenisMasculino.html', login_form=loginform)

@app.route("/masculino_acessorios")
def masculino_acessorios():
    loginform = LoginForm()
    return render_template('acessoriosMasculino.html', login_form=loginform)