from flask import Flask
from pymysql import connect
from flask_login import LoginManager
from ecommerce.models.tables import Usuario

app = Flask(__name__)
app.config.from_object('config')

db = connect(host='nicollasprado.mysql.pythonanywhere-services.com', port=3306, user='nicollasprado', password='ecommerce14', database='nicollasprado$ecommerce')

lm = LoginManager(app)

from ecommerce.controllers import main
