from flask import request, current_app
from pdf_decryptor.server.blueprints import create_blueprint

blueprint = create_blueprint("decrypt", __name__)


@blueprint.post("/")
def decrypt():
    if "file" not in request.form:
        return {
            "statusCode": 400,
            "message": "NOK"
        }

    file = request.form["file"]

