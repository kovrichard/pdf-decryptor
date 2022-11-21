import datetime

from flask import render_template

from pdf_decryptor.server.blueprints import create_blueprint

blueprint = create_blueprint("main", __name__)


@blueprint.get("/")
def main():
    return render_template("main.html", year=datetime.date.today().year)
