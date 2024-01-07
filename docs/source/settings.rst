

.. _settings:

========
Settings
========

.. _svelte_jsoneditor_props:

SVELTE_JSONEDITOR_PROPS
=======================

This setting allows modification of ``svelte-jsoneditor`` default properties for all widgets rendered in your app.

See :ref:`Editor Properties <editor_properties>` for more details and the full list of properties.

.. code-block:: py

    # settings.py

    SVELTE_JSONEDITOR_PROPS = {
        # You don't have to supply all of them, just the subset to customize
        "mode": "tree",
        "mainMenuBar": True,
        "navigationBar": True,
        "statusBar": True,
        "askToFormat": True,
        "readOnly": False,
        "indentation": 4,
        "tabSize": 4,
        "escapeControlCharacters": False,
        "escapeUnicodeCharacters": False,
        "flattenColumns": True,
    }
