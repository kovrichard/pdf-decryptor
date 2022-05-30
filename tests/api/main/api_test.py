from truth.truth import AssertThat

from tests import AppTestCase, TemplateRenderMixin, TestClientMixin


class TestMain(TestClientMixin, TemplateRenderMixin, AppTestCase):
    def test_main_renders_template(self):
        self.client.get("/")
        template, _ = self.rendered_templates[0]

        AssertThat(template.name).IsEqualTo("main.html")
