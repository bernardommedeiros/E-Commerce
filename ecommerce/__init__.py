from flask import Flask

app = Flask(__name__)
app.config.from_object('config')

from ecommerce.controllers import main
