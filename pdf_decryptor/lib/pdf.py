ALLOWED_EXTENSIONS = ["pdf"]


def allowed_extension(filename):
    return (
        "." in filename
        and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS
    )
