import unittest

from flask import template_rendered

from pdf_decryptor.server.factory import create_app


class AppTestCase(unittest.TestCase):
    def __init__(self, methodName):
        self.app = create_app()
        super().__init__(methodName)


class TestClientMixin:
    def run(self, result=None):
        with self.app.test_client() as client:
            self.client = client
            super().run(result)


class TemplateRenderMixin:
    def run(self, result=None):
        self.rendered_templates = []

        def record(sender, template, context, **extra):
            self.rendered_templates.append((template, context))

        template_rendered.connect(record, self.app)
        super().run(result)
        template_rendered.disconnect(record, self.app)
