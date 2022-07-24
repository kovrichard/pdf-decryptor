import os

from flask import current_app, redirect, request, url_for
from werkzeug.utils import secure_filename

from pdf_decryptor.lib import pdf
from pdf_decryptor.server.blueprints import create_blueprint

blueprint = create_blueprint("decrypt", __name__)


@blueprint.post("/")
def decrypt():
    bad_request = {"statusCode": 400, "message": "NOK"}

    if "file" not in request.files:
        return bad_request

    file = request.files["file"]

    if file.filename == "":
        return bad_request

    if not pdf.allowed_extension(file.filename):
        return bad_request

    filename = secure_filename(file.filename)
    file.save(os.path.join(current_app.config["UPLOAD_FOLDER"], filename))

    return redirect(url_for("main.main"))
