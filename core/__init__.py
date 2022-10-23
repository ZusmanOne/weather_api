from flask import Flask
from config import BaseConfig
from flask_caching import Cache

""" здесь инициаоизируются все объекты устанавливамемых расширений"""

app = Flask(__name__)
app.config.from_object(BaseConfig)
cache = Cache(app)
from core import routes

