from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

# from app import api1, api2, api3 .. etc
from app import routes
