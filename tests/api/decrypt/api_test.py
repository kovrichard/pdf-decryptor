import io

from truth.truth import AssertThat

from tests import AppTestCase, TemplateRenderMixin, TestClientMixin


class TestDecrypt(TestClientMixin, TemplateRenderMixin, AppTestCase):
    def test_decrypt_file_should_be_in_request(self):
        r = self.client.post("/decrypt/")

        _assert_bad_request(r)

    def test_decrypt_no_file_is_not_allowed(self):
        payload = {"file": (io.BytesIO(b"abcd"), "")}
        r = self.client.post("/decrypt/", data=payload)

        _assert_bad_request(r)

    def test_decrypt_only_pdf_can_be_uploaded(self):
        payload = {"file": (io.BytesIO(b"abcd"), "test2.pdf")}
        r = self.client.post("/decrypt/", data=payload)

        AssertThat(r.status_code).IsEqualTo(302)


def _assert_bad_request(msg):
    AssertThat(msg.json["statusCode"]).IsEqualTo(400)
    AssertThat(msg.json["message"]).IsEqualTo("NOK")
