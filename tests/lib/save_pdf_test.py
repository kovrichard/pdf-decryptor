import unittest

from ddt import data, ddt
from truth.truth import AssertThat

from pdf_decryptor.lib import save_pdf


@ddt
class TestSavePdf(unittest.TestCase):
    def test_allowed_file_allows_pdf(self):
        AssertThat(save_pdf.allowed_file("a.pdf")).IsTrue()

    @data("a.png", "a.docx", "a.jpg", "a.mp4", "a.exe", "a.sh")
    def test_allowed_file_does_not_allow_other_files(self, filename):
        AssertThat(save_pdf.allowed_file(filename)).IsFalse()

    def test_allowed_file_files_requires_an_extension(self):
        AssertThat(save_pdf.allowed_file("no_extension_file")).IsFalse()
