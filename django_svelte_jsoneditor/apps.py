from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class DjangoSvelteJsonEditorAppConfig(AppConfig):
    """Django application metadata and config"""

    name = "django_svelte_jsoneditor"
    label = "django_svelte_jsoneditor"
    verbose_name = _("Django Svelte JSONEditor")
