.. _getting_started:

===============
Getting Started
===============

.. TIP::
    A **complete example of a working server** is provided in `the tests folder of the source code <https://github.com/octue/django-svelte-jsoneditor/tree/main/tests/server>`_.

.. _install_the_library

Install the library
===================

**django-svelte-jsoneditor** is available on `pypi <https://pypi.org/project/django-svelte-jsoneditor/>`_, so installation into your python virtual environment is
simple:

.. code-block:: py

    poetry add django-svelte-jsoneditor

Not using poetry? It's highly opinionated, but it's your friend. Google it. If you're not sold, pip still works fine!


.. _install_the_django_app:

Install the django app
======================

Next, you'll need to install this as an app in your django settings:

.. code-block:: py

    INSTALLED_APPS = [
        # ...
        'django_svelte_jsoneditor'
        # ...
    ]


.. _usage:

Usage
=====

The ``SvelteJSONEditorWidget`` adds editor capabilities to JSON fields in Django.

Below you can see an example of how to override the default widget (textarea) for JSONFields in the django admin.

.. code-block:: py

    # admin.py

    from django.contrib import admin
    from django_svelte_jsoneditor.widgets import SvelteJSONEditorWidget

    from .models import MyModel


    @admin.register(MyModel)
    class MyModelAdmin(admin.ModelAdmin):
        formfield_overrides = {
            models.JSONField: {
                "widget": SvelteJSONEditorWidget,
            }
        }

Another example is how to create a new Django form integrating SvelteJSONEditorWidget, replacing the TextArea widget.

.. code-block:: py

    # forms.py
    from django import forms
    from django_svelte_jsoneditor.widgets import SvelteJSONEditorWidget


    class MyJSONEditorForm(forms.Form):
        json = forms.JSONField(widgets=SvelteJSONEditorWidget())
