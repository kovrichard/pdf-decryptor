import os

from pdf_decryptor.server import config


def decrypt(filename, password):
    file, ext = os.path.splitext(filename)
    outputname = f"{file}_decrypted{ext}"

    os.system(
        f"qpdf --decrypt --password={password} {os.path.join(config.UPLOAD_FOLDER, filename)} {os.path.join(config.UPLOAD_FOLDER, outputname)}"
    )

    return outputname
