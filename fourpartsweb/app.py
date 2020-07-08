from flask import Flask
import os

from fourpartsweb.blueprints.index import index
from fourpartsweb.blueprints.download import download
from fourpartsweb.api.v1.midifile import MidifileView

from fourpartsweb.extensions import (
    debug_toolbar,
    db,
    marshmallow
)


def create_app():
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object('config.settings')
    app.register_blueprint(index)
    app.register_blueprint(download)

    extensions(app)

    MidifileView.register(app)

    try: 
        os.makedirs(app.config["MIDISTORE_PATH"])
        os.makedirs(app.config["RESULTSTORE_PATH"])
    except FileExistsError:
        pass

    return app


def extensions(app):
    debug_toolbar.init_app(app)
    db.init_app(app)
    marshmallow.init_app(app)

    return None
