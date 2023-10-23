from django.contrib import admin

from tests.server.example.models import (
    ExampleJsonFieldModel,
    ExampleBlankJsonFieldModel,
    ExampleUneditableJsonFieldModel,
)


class ExampleJsonFieldModelAdmin(admin.ModelAdmin):
    """A basic admin panel to demonstrate the direct upload storage behaviour"""


class ExampleBlankJsonFieldModelAdmin(admin.ModelAdmin):
    """A basic admin panel to demonstrate the direct upload storage behaviour where blank=True"""


class ExampleUneditableJsonFieldModelAdmin(admin.ModelAdmin):
    """A basic admin panel to demonstrate the direct upload storage behaviour where blank=True"""


admin.site.register(ExampleJsonFieldModel, ExampleJsonFieldModelAdmin)
admin.site.register(ExampleBlankJsonFieldModel, ExampleBlankJsonFieldModelAdmin)
admin.site.register(ExampleUneditableJsonFieldModel, ExampleUneditableJsonFieldModelAdmin)
