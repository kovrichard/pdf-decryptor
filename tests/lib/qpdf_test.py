import os
import unittest

from truth.truth import AssertThat

from pdf_decryptor.lib import qpdf
from pdf_decryptor.server import config


class TestQpdf(unittest.TestCase):
    test_output = os.path.join(config.UPLOAD_FOLDER, "test_decrypted.pdf")

    def setUp(self):
        if os.path.exists(self.test_output):
            os.remove(self.test_output)

    def test_qpdf_returns_decrypted_file_name(self):
        filename = qpdf.decrypt("test.pdf", "testpass")

        AssertThat(filename).IsEqualTo("test_decrypted.pdf")

    def test_qpdf_creates_decrypted_file(self):
        qpdf.decrypt("test.pdf", "testpass")

        AssertThat(os.path.exists(self.test_output)).IsTrue()
