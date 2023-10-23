from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ExampleAppConfig(AppConfig):
    """Example (test server) app showing how you would use django-svelte-jsoneditor within your own django server"""

    name = "tests.server.example"
    label = "example"
    verbose_name = _("Example App using Django Svelte JSONEditor")
