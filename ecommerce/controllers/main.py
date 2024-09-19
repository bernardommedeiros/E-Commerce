from flask import render_template, flash, redirect, url_for
from flask_login import login_user, logout_user
from ecommerce import app, db, lm

from ecommerce.models.tables import Usuario
from ecommerce.models.forms import LoginForm, RegisterForm

usuarioOBJ = Usuario()

@lm.user_loader
def load_user(id):
    return usuarioOBJ

@app.route("/home", methods=["GET", "POST"])
@app.route("/index", methods=["GET", "POST"])
@app.route("/", methods=["GET", "POST"])
def index():
    loginform = LoginForm()
    if(loginform.validate_on_submit()):
        cursor = db.cursor()
        usuarioDB = cursor.execute("SELECT * FROM users WHERE usuario =%s and senha =%s", (loginform.usuario.data, loginform.senha.data))
        if(usuarioDB > 0):
            cursorId = db.cursor()
            cursorId.execute("SELECT id FROM users WHERE usuario=%s and senha=%s", (loginform.usuario.data, loginform.senha.data))
            cursorEmail = db.cursor()
            cursorEmail.execute("SELECT email FROM users WHERE usuario=%s and senha=%s", (loginform.usuario.data, loginform.senha.data))
            usuarioOBJ.instanciar(cursorId.fetchone()[0], loginform.usuario.data, cursorEmail.fetchone()[0], loginform.senha.data)
            login_user(usuarioOBJ)
            flash(f"Logado com sucesso!")
        else:
            flash("Usuário ou senha inválido(s)")
    return render_template('index.html', login_form=loginform, usuario=usuarioOBJ)

@app.route("/feminino_vestuario", methods=["GET", "POST"])
def feminino():
    loginform = LoginForm()
    if(loginform.validate_on_submit()):
        cursor = db.cursor()
        usuarioDB = cursor.execute("SELECT * FROM users WHERE usuario =%s and senha =%s", (loginform.usuario.data, loginform.senha.data))
        if(usuarioDB > 0):
            cursorId = db.cursor()
            cursorId.execute("SELECT id FROM users WHERE usuario=%s and senha=%s", (loginform.usuario.data, loginform.senha.data))
            cursorEmail = db.cursor()
            cursorEmail.execute("SELECT email FROM users WHERE usuario=%s and senha=%s", (loginform.usuario.data, loginform.senha.data))
            usuarioOBJ.instanciar(cursorId.fetchone()[0], loginform.usuario.data, cursorEmail.fetchone()[0], loginform.senha.data)
            login_user(usuarioOBJ)
            flash(f"Logado com sucesso!")
        else:
            flash("Usuário ou senha inválido(s)")
    return render_template('feminino.html', login_form=loginform, usuario=usuarioOBJ)

@app.route("/feminino_tenis", methods=["GET", "POST"])
def feminino_tenis():
    loginform = LoginForm()
    if(loginform.validate_on_submit()):
        cursor = db.cursor()
        usuarioDB = cursor.execute("SELECT * FROM users WHERE usuario =%s and senha =%s", (loginform.usuario.data, loginform.senha.data))
        if(usuarioDB > 0):
            cursorId = db.cursor()
            cursorId.execute("SELECT id FROM users WHERE usuario=%s and senha=%s", (loginform.usuario.data, loginform.senha.data))
            cursorEmail = db.cursor()
            cursorEmail.execute("SELECT email FROM users WHERE usuario=%s and senha=%s", (loginform.usuario.data, loginform.senha.data))
            usuarioOBJ.instanciar(cursorId.fetchone()[0], loginform.usuario.data, cursorEmail.fetchone()[0], loginform.senha.data)
            login_user(usuarioOBJ)
            flash(f"Logado com sucesso!")
        else:
            flash("Usuário ou senha inválido(s)")
    return render_template('tenisFeminino.html', login_form=loginform, usuario=usuarioOBJ)

@app.route("/feminino_acessorios", methods=["GET", "POST"])
def feminino_acessorios():
    loginform = LoginForm()
    if(loginform.validate_on_submit()):
        cursor = db.cursor()
        usuarioDB = cursor.execute("SELECT * FROM users WHERE usuario =%s and senha =%s", (loginform.usuario.data, loginform.senha.data))
        if(usuarioDB > 0):
            cursorId = db.cursor()
            cursorId.execute("SELECT id FROM users WHERE usuario=%s and senha=%s", (loginform.usuario.data, loginform.senha.data))
            cursorEmail = db.cursor()
            cursorEmail.execute("SELECT email FROM users WHERE usuario=%s and senha=%s", (loginform.usuario.data, loginform.senha.data))
            usuarioOBJ.instanciar(cursorId.fetchone()[0], loginform.usuario.data, cursorEmail.fetchone()[0], loginform.senha.data)
            login_user(usuarioOBJ)
            flash(f"Logado com sucesso!")
        else:
            flash("Usuário ou senha inválido(s)")
    return render_template('acessoriosFeminino.html', login_form=loginform, usuario=usuarioOBJ)

@app.route("/masculino_vestuario", methods=["GET", "POST"])
def masculino():
    loginform = LoginForm()
    if(loginform.validate_on_submit()):
        cursor = db.cursor()
        usuarioDB = cursor.execute("SELECT * FROM users WHERE usuario =%s and senha =%s", (loginform.usuario.data, loginform.senha.data))
        if(usuarioDB > 0):
            cursorId = db.cursor()
            cursorId.execute("SELECT id FROM users WHERE usuario=%s and senha=%s", (loginform.usuario.data, loginform.senha.data))
            cursorEmail = db.cursor()
            cursorEmail.execute("SELECT email FROM users WHERE usuario=%s and senha=%s", (loginform.usuario.data, loginform.senha.data))
            usuarioOBJ.instanciar(cursorId.fetchone()[0], loginform.usuario.data, cursorEmail.fetchone()[0], loginform.senha.data)
            login_user(usuarioOBJ)
            flash(f"Logado com sucesso!")
        else:
            flash("Usuário ou senha inválido(s)")
    return render_template('masculino.html', login_form=loginform, usuario=usuarioOBJ)

@app.route("/masculino_tenis", methods=["GET", "POST"])
def masculino_tenis():
    loginform = LoginForm()
    if(loginform.validate_on_submit()):
        cursor = db.cursor()
        usuarioDB = cursor.execute("SELECT * FROM users WHERE usuario =%s and senha =%s", (loginform.usuario.data, loginform.senha.data))
        if(usuarioDB > 0):
            cursorId = db.cursor()
            cursorId.execute("SELECT id FROM users WHERE usuario=%s and senha=%s", (loginform.usuario.data, loginform.senha.data))
            cursorEmail = db.cursor()
            cursorEmail.execute("SELECT email FROM users WHERE usuario=%s and senha=%s", (loginform.usuario.data, loginform.senha.data))
            usuarioOBJ.instanciar(cursorId.fetchone()[0], loginform.usuario.data, cursorEmail.fetchone()[0], loginform.senha.data)
            login_user(usuarioOBJ)
            flash(f"Logado com sucesso!")
        else:
            flash("Usuário ou senha inválido(s)")
    return render_template('tenisMasculino.html', login_form=loginform, usuario=usuarioOBJ)

@app.route("/masculino_acessorios", methods=["GET", "POST"])
def masculino_acessorios():
    loginform = LoginForm()
    if(loginform.validate_on_submit()):
        cursor = db.cursor()
        usuarioDB = cursor.execute("SELECT * FROM users WHERE usuario =%s and senha =%s", (loginform.usuario.data, loginform.senha.data))
        if(usuarioDB > 0):
            cursorId = db.cursor()
            cursorId.execute("SELECT id FROM users WHERE usuario=%s and senha=%s", (loginform.usuario.data, loginform.senha.data))
            cursorEmail = db.cursor()
            cursorEmail.execute("SELECT email FROM users WHERE usuario=%s and senha=%s", (loginform.usuario.data, loginform.senha.data))
            usuarioOBJ.instanciar(cursorId.fetchone()[0], loginform.usuario.data, cursorEmail.fetchone()[0], loginform.senha.data)
            login_user(usuarioOBJ)
            flash(f"Logado com sucesso!")
        else:
            flash("Usuário ou senha inválido(s)")
    return render_template('acessoriosMasculino.html', login_form=loginform, usuario=usuarioOBJ)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("index"))

@app.route("/registrar", methods=["GET", "POST"])
def registrar():
    registerForm = RegisterForm()
    if(registerForm.validate_on_submit()):
        cursor = db.cursor()
        existeNoDB = cursor.execute("SELECT * FROM users WHERE usuario =%s and email=%s", (registerForm.usuario.data, registerForm.email.data))
        if(existeNoDB == 0):
            cursor.execute("INSERT INTO users (usuario, email, senha) values (%s, %s, %s)", (registerForm.usuario.data, registerForm.email.data, registerForm.senha.data))
            cursor.connection.commit()
            flash(f"Conta criada com sucesso!")
        else:
            flash(f"O usuário {registerForm.usuario.data} ou o email {registerForm.email.data} já existem no nosso banco de dados")
    return render_template('registrar.html', register_form=registerForm)

@app.route("/gerenciador_usuarios", methods=["GET", "POST"])
def gerenciador_usuarios():
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users WHERE id > 3")
    users = cursor.fetchall()
    return render_template('gerenciadorUsuarios.html', users = users)