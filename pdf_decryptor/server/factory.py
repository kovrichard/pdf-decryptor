from flask import Flask
from flask_cors import CORS

from pdf_decryptor.api.decrypt.api import blueprint as decrypt_bp


def create_app():
    app = Flask(
        __name__, template_folder="base_templates", static_folder="static"
    )
    app.config.from_object("pdf_decryptor.server.config")

    __configure_cors(app)

    app.register_blueprint(decrypt_bp, url_prefix="/decrypt")

    return app


def __configure_cors(app):
    CORS(app, origins=app.config.get("CORS_DOMAINS"))
