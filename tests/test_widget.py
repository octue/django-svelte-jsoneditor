# Disabled for testing:
# pylint: disable=missing-docstring
# pylint: disable=protected-access
# pylint: disable=too-many-public-methods

from django.contrib.auth.models import User
from django.test import Client, TestCase

from tests.server.example.models import ExampleBlankJsonFieldModel, ExampleJsonFieldModel
from ._utils import get_admin_add_view_url, get_admin_change_view_url


class TestJsonFieldAdmin(TestCase):
    @classmethod
    def setUpTestData(cls):
        """Set up data for the whole test case (used within the outer transaction to increase speed)"""
        User.objects.create_superuser(username="superuser", password="secret", email="admin@example.com")

    def setUp(self, *args, **kwargs):
        """Log in the superuser"""
        super().setUp(*args, **kwargs)
        self.client = Client()
        self.client.login(username="superuser", password="secret")

    def test_add_view_loads_normally(self):
        response = self.client.get(get_admin_add_view_url(ExampleJsonFieldModel))
        self.assertEqual(response.status_code, 200)

    def test_change_view_loads_normally(self):
        """Ensure we can load a change view"""

        obj = ExampleJsonFieldModel.objects.create()

        # Assert that the view loads
        response = self.client.get(get_admin_change_view_url(obj))
        self.assertEqual(response.status_code, 200)

        # Assert the widget contents
        # widget = response.context_data["adminform"].fields["blob"].widget
        # self.assertTrue(hasattr(widget, "signed_ingress_url"))
        # self.assertTrue(
        #     widget.signed_ingress_url.startswith("https://storage.googleapis.com/example-media-assets/_tmp")
        # )

    def test_blank_add_view_loads_normally(self):
        response = self.client.get(get_admin_add_view_url(ExampleBlankJsonFieldModel))
        self.assertEqual(response.status_code, 200)
