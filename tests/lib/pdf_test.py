import unittest

from ddt import data, ddt
from truth.truth import AssertThat

from pdf_decryptor.lib import pdf


@ddt
class TestSavePdf(unittest.TestCase):
    def test_allowed_file_allows_pdf(self):
        AssertThat(pdf.allowed_extension("a.pdf")).IsTrue()

    @data("a.png", "a.docx", "a.jpg", "a.mp4", "a.exe", "a.sh")
    def test_allowed_file_does_not_allow_other_files(self, filename):
        AssertThat(pdf.allowed_extension(filename)).IsFalse()

    def test_allowed_file_files_requires_an_extension(self):
        AssertThat(pdf.allowed_extension("no_extension_file")).IsFalse()
