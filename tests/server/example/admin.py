from django.contrib import admin
from django.db import models
from django_svelte_jsoneditor.widgets import SvelteJSONEditorWidget

from tests.server.example.models import (
    ExampleBlankJsonFieldModel,
    ExampleJsonFieldModel,
    ExampleUneditableJsonFieldModel,
    ExampleMultipleJsonFieldModel,
)


class ExampleJsonFieldModelAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.JSONField: {
            "widget": SvelteJSONEditorWidget,
        }
    }


class ExampleBlankJsonFieldModelAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.JSONField: {
            "widget": SvelteJSONEditorWidget,
        }
    }


class ExampleUneditableJsonFieldModelAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.JSONField: {
            "widget": SvelteJSONEditorWidget,
        }
    }


class ExampleMultipleJsonFieldModelAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.JSONField: {
            "widget": SvelteJSONEditorWidget,
        }
    }


admin.site.register(ExampleJsonFieldModel, ExampleJsonFieldModelAdmin)
admin.site.register(ExampleBlankJsonFieldModel, ExampleBlankJsonFieldModelAdmin)
admin.site.register(ExampleUneditableJsonFieldModel, ExampleUneditableJsonFieldModelAdmin)
admin.site.register(ExampleMultipleJsonFieldModel, ExampleMultipleJsonFieldModelAdmin)
