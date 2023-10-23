.. _getting_started:

===============
Getting Started
===============

.. TIP::
    A **complete example of a working server** is provided in `the tests folder of the source code <https://github.com/octue/django-svelte-jsoneditor/tree/main/tests/server>`_.

.. _install_the_library

Install the library
===================

**django-svelte-jsoneditor** is available on `pypi <https://pypi.org/>`_, so installation into your python virtual environment is dead
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
