from truth.truth import AssertThat

from tests import AppTestCase, TemplateRenderMixin, TestClientMixin


class TestDecrypt(TestClientMixin, TemplateRenderMixin, AppTestCase):
    def test_decrypt_file_should_be_in_request(self):
        r = self.client.post("/decrypt/")

        AssertThat(r.json["statusCode"]).IsEqualTo(400)
        AssertThat(r.json["message"]).IsEqualTo("NOK")
