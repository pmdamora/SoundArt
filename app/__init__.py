# SoundArt
# Copyright 2018 pauldamora.com All rights reserved
#
# Authors: Paul D'Amora
#
# Description: Initiates the app

from flask import Flask
from app.config import Config


# Initialize the app from configuration file
app = Flask(__name__)
app.config.from_object(Config)


app.config["flask_profiler"] = {
    "enabled": False,
    "storage": {
        "engine": "sqlite"
    },
    "basicAuth": {
        "enabled": True,
        "username": "admin",
        "password": "admin"
    },
    "ignore": [
        "^/static/.*"
    ]
}

from app import routes
