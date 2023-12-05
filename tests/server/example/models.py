from django.db.models import JSONField, Model


class ExampleJsonFieldModel(Model):
    """
    An example model containing a JsonField
    """

    my_json = JSONField()

    class Meta:
        """Metaclass defining this model to reside in the example app"""

        app_label = "example"


class ExampleBlankJsonFieldModel(Model):
    """
    As ExampleJsonFieldModel but showing blankable behaviour
    (This is mostly used for widget development and testing)
    """

    my_json = JSONField(
        blank=True,
        null=True,
    )

    class Meta:
        """Metaclass defining this model to reside in the example app"""

        app_label = "example"


class ExampleUneditableJsonFieldModel(Model):
    """
    As ExampleJsonFieldModel but showing behaviour when editable=False
    (This is mostly used for widget development and testing)
    """

    my_json = JSONField(blank=True, null=True, editable=False)

    class Meta:
        """Metaclass defining this model to reside in the example app"""

        app_label = "example"


class ExampleMultipleJsonFieldModel(Model):
    """
    Multiple JSON fields in one model to test correct behaviour of JavaScript
    """

    my_json1 = JSONField()
    my_json2 = JSONField()
    my_json3 = JSONField()

    class Meta:
        """Metaclass defining this model to reside in the example app"""

        app_label = "example"
