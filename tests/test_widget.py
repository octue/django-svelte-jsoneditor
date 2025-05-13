# Disabled for testing:
# pylint: disable=missing-docstring
# pylint: disable=protected-access
# pylint: disable=too-many-public-methods

from django import forms
from django.contrib.auth.models import User
from django.test import Client, TestCase
from django.test.utils import override_settings
from django_svelte_jsoneditor.exceptions import InvalidPropError
from django_svelte_jsoneditor.widgets import SvelteJSONEditorWidget, ReadOnlySvelteJSONEditorWidget

from tests.server.example.models import ExampleBlankJsonFieldModel, ExampleJsonFieldModel
from ._utils import get_admin_add_view_url, get_admin_change_view_url


class BaseTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        """Set up data for the whole test case (used within the outer transaction to increase speed)"""
        User.objects.create_superuser(username="superuser", password="secret", email="admin@example.com")

    def setUp(self, *args, **kwargs):
        """Log in the superuser"""
        super().setUp(*args, **kwargs)
        self.client = Client()
        self.client.login(username="superuser", password="secret")


class TestJsonFieldAdmin(BaseTestCase):
    def test_add_view_loads_normally(self):
        response = self.client.get(get_admin_add_view_url(ExampleJsonFieldModel))
        self.assertEqual(response.status_code, 200)

    def test_blank_add_view_loads_normally(self):
        response = self.client.get(get_admin_add_view_url(ExampleBlankJsonFieldModel))
        self.assertEqual(response.status_code, 200)

    def test_change_view_loads_normally(self):
        obj = ExampleJsonFieldModel(my_json={"one": "two"})
        obj.save()

        response = self.client.get(get_admin_change_view_url(obj))
        self.assertEqual(response.status_code, 200)


class TestSvelteJsonEditorAdmin(BaseTestCase):
    def test_change_view_default_global_settings(self):
        obj = ExampleJsonFieldModel(my_json={"one": "two"})
        obj.save()

        response = self.client.get(get_admin_change_view_url(obj))
        self.assertContains(response, '"readOnly": false')

    @override_settings(SVELTE_JSONEDITOR={})
    def test_change_view_empty_global_settings(self):
        obj = ExampleJsonFieldModel(my_json={"one": "two"})
        obj.save()

        response = self.client.get(get_admin_change_view_url(obj))
        self.assertContains(response, '"readOnly": false')

    @override_settings(SVELTE_JSONEDITOR_PROPS={**{"readOnly": True}})
    def test_change_view_modified_global_settings(self):
        obj = ExampleJsonFieldModel(my_json={"one": "two"})
        obj.save()

        response = self.client.get(get_admin_change_view_url(obj))
        self.assertContains(response, '"readOnly": true')


class TestSvelteJsonEditorWidget(TestCase):
    def test_svelte_jsoneditor_widget_default_props(self):
        class SvelteJsonEditorForm(forms.Form):
            my_json = forms.JSONField(widget=SvelteJSONEditorWidget())

        form = SvelteJsonEditorForm()
        self.assertIn('"readOnly": false', str(form["my_json"]))

    def test_svelte_jsoneditor_widget_custom_props(self):
        class SvelteJsonEditorForm(forms.Form):
            my_json = forms.JSONField(widget=SvelteJSONEditorWidget(props={"readOnly": True}))

        form = SvelteJsonEditorForm()

        self.assertIn('"readOnly": true', str(form["my_json"]))

    @override_settings(SVELTE_JSONEDITOR_PROPS={**{"readOnly": True}})
    def test_svelte_jsoneditor_widget_global_props(self):
        class SvelteJsonEditorForm(forms.Form):
            my_json = forms.JSONField(widget=SvelteJSONEditorWidget())

        form = SvelteJsonEditorForm()
        self.assertIn('"readOnly": true', str(form["my_json"]))

    @override_settings(SVELTE_JSONEDITOR_PROPS={**{"readOnly": True}})
    def test_svelte_jsoneditor_widget_overridden_props(self):
        class SvelteJsonEditorForm(forms.Form):
            my_json = forms.JSONField(widget=SvelteJSONEditorWidget(props={"readOnly": False}))

        form = SvelteJsonEditorForm()
        self.assertIn('"readOnly": false', str(form["my_json"]))

    @override_settings(SVELTE_JSONEDITOR_PROPS={**{"incorrectProp": True}})
    def test_svelte_jsoneditor_widget_incorrect_props(self):

        # for props at the widget level
        with self.assertRaises(InvalidPropError):
            SvelteJSONEditorWidget(props={"incorrectProp": True})

        # for props in settings
        with self.assertRaises(InvalidPropError):
            widget = SvelteJSONEditorWidget()
            widget.get_context("my_json", "null", {"required": True, "id": "id_my_json"})

class TestReadOnlySvelteJSONEditorWidget(TestCase):
    def test_readonly_widget_default_props(self):
        """Test that ReadOnlySvelteJSONEditorWidget has the correct default props."""
        class ReadOnlyJsonEditorForm(forms.Form):
            my_json = forms.JSONField(widget=ReadOnlySvelteJSONEditorWidget())

        form = ReadOnlyJsonEditorForm()
        widget_html = str(form["my_json"])
        
        # Check that all expected props are set correctly
        self.assertIn('"mode": "view"', widget_html)
        self.assertIn('"readOnly": true', widget_html)
        self.assertIn('"navigationBar": false', widget_html)
    
