from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, EmailField
from wtforms.validators import DataRequired, Email


class LoginForm(FlaskForm):
    usuario = StringField("usuario", validators=[DataRequired()])
    senha = PasswordField("senha", validators=[DataRequired()])
    lembrar_senha = BooleanField("lembrar_senha")

class RegisterForm(FlaskForm):
    usuario = StringField("usuario", validators=[DataRequired()])
    email = EmailField("email", validators=[DataRequired(), Email()])
    senha = PasswordField("senha", validators=[DataRequired()])
    termo = BooleanField("termo", validators=[DataRequired()])