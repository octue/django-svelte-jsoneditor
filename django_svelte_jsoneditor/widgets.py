import json
from django.forms import Textarea

from .settings import check_props, get_props


class SvelteJSONEditorWidget(Textarea):
    template_name = "django_svelte_jsoneditor/widgets/svelte_jsoneditor.html"

    def __init__(self, props=None, attrs=None, wrapper_class="svelte-jsoneditor-wrapper"):
        if attrs is None:
            attrs = {}

        self.props = {} if props is None else props.copy()
        self.wrapper_class = wrapper_class

        check_props(self.props)
        attrs.update({"class": "hidden"})

        super().__init__(attrs)

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        context["widget"].update({"props": json.dumps({**get_props(), **self.props})})
        context["widget"].update({"wrapper_class": self.wrapper_class})
        return context

    class Media:
        css = {"all": ("django_svelte_jsoneditor/css/svelte_jsoneditor.css",)}

class ReadOnlySvelteJSONEditorWidget(SvelteJSONEditorWidget):
    def __init__(self, attrs=None):
        props = {
            'mode': 'view',
            'readOnly': True,
            'navigationBar': False
        }
        super().__init__(props=props, attrs=attrs)
