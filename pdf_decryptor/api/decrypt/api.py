import os

from flask import current_app, request, send_file
from werkzeug.utils import secure_filename

from pdf_decryptor.lib import pdf, qpdf
from pdf_decryptor.server.blueprints import create_blueprint

blueprint = create_blueprint("decrypt", __name__)


@blueprint.post("/")
def decrypt():
    if "file" not in request.files:
        return __bad_request("Missing file")

    file = request.files["file"]

    if file.filename == "":
        return __bad_request("Empty filename")

    if not pdf.allowed_extension(file.filename):
        return __bad_request("Extension not allowed")

    if "password" not in request.form or request.form["password"] == "":
        return __bad_request("Missing password")

    filename = secure_filename(file.filename)
    filename = os.path.join(current_app.config["UPLOAD_FOLDER"], filename)
    file.save(filename)

    qpdf.decrypt(filename, request.form["password"])

    return send_file(
        f"{os.path.splitext(filename)[0]}_decrypted.pdf",
        mimetype="application/pdf",
        as_attachment=True,
    )


def __bad_request(message="NOK") -> dict:
    return message, 400
