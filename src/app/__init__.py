from . import views
from flask import Flask


app = Flask(__name__)

views.init(app)
