
.. _editor_properties:

=================
Editor Properties
=================

The ``svelte-jsoneditor`` has a range of properties allowing customisation of appearance and function. The ``SvelteJSONEditorWidget`` allows you to alter ``svelte-jsoneditor``'s defaults.

.. ATTENTION::
    Not all ``svelte-jsoneditor`` properties are configurable, notably the ``on*`` callbacks. To add such callbacks you'd need to override the widget template yourself, since they require javascript functions.


.. _available_properties:

Available Properties
====================

Official documentation and descriptions are available on `the svelte-jsoneditor GitHub page <https://github.com/josdejong/svelte-jsoneditor#properties>`_.

 ========================= ============================= =========
  Property                  Type                          Default
 ========================= ============================= =========
  mode                      'tree' or 'text' or 'table'   'tree'
  mainMenuBar               boolean                       True
  navigationBar             boolean                       True
  statusBar                 boolean                       True
  askToFormat               boolean                       True
  readOnly                  boolean                       False
  indentation               number or string              4
  tabSize                   number                        4
  escapeControlCharacters   boolean                       False
  escapeUnicodeCharacters   boolean                       False
  flattenColumns            boolean                       True
 ========================= ============================= =========


.. _using_properties:

Using Properties
================

To alter the default properties used by ALL widgets in your application, see the :ref:`SVELTE_JSONEDITOR_PROPS <svelte_jsoneditor_props>` setting.

To alter the widget for an individual field, the ``SvelteJSONEditorWidget`` accepts an additional argument, ``props``. The following example shows this used in a form:

.. code-block:: py

    # forms.py

    from django import forms


    class SvelteJsonEditorForm(forms.Form):
        my_json = forms.JSONField(widget=SvelteJSONEditorWidget(props={
            "readOnly": True
        }))


Or to use custom widget properties in the django admin:

.. code-block:: py

    # admin.py

    from django import forms
    from django.contrib import admin

    from .models import ExampleModel

    class CustomForm(forms.ModelForm):
        class Meta:
            model = ExampleModel
            fields = "__all__"

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields["some_json_field"].widget = SvelteJSONEditorWidget(props={"readOnly": True})


    @admin.register(ExampleModel, ExampleModelAdmin)
    class ExampleModelAdmin(admin.ModelAdmin):
        form = CustomForm
        formfield_overrides = {
            models.JSONField: {
                "widget": SvelteJSONEditorWidget,
            }
        }







.. # settings.py

.. SVELTE_JSONEDITOR_PROPS = {
..     "mode": "tree",
..     "mainMenuBar": True,
..     "navigationBar": True,
..     "statusBar": True,
..     "askToFormat": True,
..     "readOnly": False,
..     "indentation": 4,
..     "tabSize": 4,
..     "escapeControlCharacters": False,
..     "escapeUnicodeCharacters": False,
..     "flattenColumns": True,
.. }
.. ```
