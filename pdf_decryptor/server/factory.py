from flask import Flask

from pdf_decryptor.api.decrypt.api import blueprint as decrypt_bp
from pdf_decryptor.api.main.api import blueprint as main_bp


def create_app():
    app = Flask(__name__, template_folder="base_templates", static_folder=None)
    app.config.from_object("pdf_decryptor.server.config")

    app.register_blueprint(main_bp, url_prefix="/")
    app.register_blueprint(decrypt_bp, url_prefix="/decrypt")

    return app
