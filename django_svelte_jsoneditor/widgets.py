import json
from django.forms import Textarea

from .settings import check_props, get_props


class SvelteJSONEditorWidget(Textarea):
    template_name = "django_svelte_jsoneditor/widgets/svelte_jsoneditor.html"

    def __init__(self, props=None, attrs=None):
        if attrs is None:
            attrs = {}

        self.props = {} if props is None else props.copy()
        check_props(self.props)
        attrs.update({"class": "hidden"})

        super().__init__(attrs)

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        context["widget"].update({"props": json.dumps({**get_props(), **self.props})})
        return context

    class Media:
        css = {"all": ("django_svelte_jsoneditor/css/svelte_jsoneditor.css",)}
