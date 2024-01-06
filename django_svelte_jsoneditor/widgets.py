import json
from django.forms import Textarea

from .settings import get_config


class SvelteJSONEditorWidget(Textarea):
    template_name = "django_svelte_jsoneditor/widgets/svelte_jsoneditor.html"

    def __init__(self, props=None, attrs=None):
        if attrs is None:
            attrs = {}

        self.props = {} if props is None else props.copy()
        attrs.update({"class": "hidden"})

        super().__init__(attrs)

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        context["widget"].update({"props": json.dumps({**get_config()["PROPS"], **self.props})})
        return context

    class Media:
        css = {"all": ("django_svelte_jsoneditor/css/svelte_jsoneditor.css",)}
