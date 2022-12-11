import io

from ddt import data, ddt
from truth.truth import AssertThat

from tests import AppTestCase, TemplateRenderMixin, TestClientMixin


@ddt
class TestDecrypt(TestClientMixin, TemplateRenderMixin, AppTestCase):
    def test_decrypt_file_should_be_in_request(self):
        r = self.client.post("/decrypt/")

        _assert_bad_request(r, "Missing file")

    def test_decrypt_no_file_is_not_allowed(self):
        payload = {"file": (io.BytesIO(b"abcd"), "")}
        r = self.client.post("/decrypt/", data=payload)

        _assert_bad_request(r, "Empty filename")

    def test_decrypt_only_pdf_extension_is_allowed(self):
        payload = {"file": (io.BytesIO(b"abcd"), "test.png")}
        r = self.client.post("/decrypt/", data=payload)

        _assert_bad_request(r, "Extension not allowed")

    def test_decrypt_pdf_can_be_uploaded(self):
        payload = {
            "file": (
                io.BytesIO(
                    b"\x25\x50\x44\x46\x2D\x31\x2E\x0D\x74\x72\x61\x69\x6C\x65\x72\x3C\x3C\x2F\x52\x6F\x6F\x74\x3C\x3C\x2F\x50\x61\x67\x65\x73\x3C\x3C\x2F\x4B\x69\x64\x73\x5B\x3C\x3C\x2F\x4D\x65\x64\x69\x61\x42\x6F\x78\x5B\x30\x20\x30\x20\x33\x20\x33\x5D\x3E\x3E\x5D\x3E\x3E\x3E\x3E\x3E\x3E"
                ),
                "test2.pdf",
            ),
            "password": "testpass",
        }
        r = self.client.post("/decrypt/", data=payload)

        AssertThat(r.status_code).IsEqualTo(200)
        AssertThat(r.headers["Content-Type"]).IsEqualTo("application/pdf")
        AssertThat(r.headers["Content-Disposition"]).Contains(
            "test2_decrypted.pdf"
        )

    def test_decrypt_password_is_required(self):
        payload = {"file": (io.BytesIO(b"abcd"), "test2.pdf")}
        r = self.client.post("/decrypt/", data=payload)

        _assert_bad_request(r, "Missing password")

    def test_decrypt_password_cannot_be_empty(self):
        payload = {"file": (io.BytesIO(b"abcd"), "test2.pdf"), "password": ""}
        r = self.client.post("/decrypt/", data=payload)

        _assert_bad_request(r, "Missing password")

    @data("http://localhost:4200", "https://pdfdecryptor.vercel.app")
    def test_decrypt_returns_cors_headers(self, origin: str) -> None:
        r = self.client.post(
            "/decrypt/",
            headers={"Origin": origin},
        )

        AssertThat(self.app.config.get("CORS_DOMAINS")).Contains(
            r.headers["Access-Control-Allow-Origin"]
        )


def _assert_bad_request(msg, response="NOK"):
    AssertThat(msg.status_code).IsEqualTo(400)
    AssertThat(msg.get_data().decode()).IsEqualTo(response)
