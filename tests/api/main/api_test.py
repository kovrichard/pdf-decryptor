import datetime

from truth.truth import AssertThat

from tests import AppTestCase, TemplateRenderMixin, TestClientMixin


class TestMain(TestClientMixin, TemplateRenderMixin, AppTestCase):
    def test_main_renders_template(self):
        self.client.get("/")
        template, _ = self.rendered_templates[0]

        AssertThat(template.name).IsEqualTo("main.html")

    def test_main_renders_current_year_into_template(self):
        self.client.get("/")
        _, context = self.rendered_templates[0]

        AssertThat(context["year"]).IsEqualTo(datetime.date.today().year)
