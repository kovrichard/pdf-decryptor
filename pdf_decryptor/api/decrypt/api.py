from flask import request

from pdf_decryptor.server.blueprints import create_blueprint

blueprint = create_blueprint("decrypt", __name__)


@blueprint.post("/")
def decrypt():
    bad_request = {"statusCode": 400, "message": "NOK"}

    if "file" not in request.form:
        return bad_request

    file = request.form["file"]

    if file.filename == "":
        return bad_request
