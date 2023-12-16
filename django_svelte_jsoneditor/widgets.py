from django.forms import Textarea


class SvelteJSONEditorWidget(Textarea):
    template_name = "django_svelte_jsoneditor/widgets/svelte_jsoneditor.html"

    def __init__(self, attrs=None):
        if attrs is None:
            attrs = {}

        attrs.update({"class": "hidden"})

        super().__init__(attrs)

    class Media:
        css = {"all": ("django_svelte_jsoneditor/css/svelte_jsoneditor.css",)}
