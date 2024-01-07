.. ATTENTION::
    This library is used for a few apps in production, but it is still early in development.
    Like the idea of it? Please
    `star us on GitHub <https://github.com/octue/django-svelte-jsoneditor>`_ and contribute via the
    `issues board <https://github.com/octue/django-svelte-jsoneditor/issues>`_.

=========================
Django Svelte JSON Editor
=========================

``django-svelte-jsoneditor`` is a for django's JSONField that allows manipulation and display of JSON data. The widget is built using Jos deJong's new `svelte-jsoneditor <https://github.com/josdejong/svelte-jsoneditor>`_.

.. |pic1| image:: images/jsoneditor_tree_mode.png
   :width: 49%
   :alt: JSONEditor in tree mode

.. |pic2| image:: images/jsoneditor_text_mode.png
   :width: 49%
   :alt: JSONEditor in text mode

|pic1| |pic2|

This app is a replacement for ``django-jsoneditor`` (which uses a deprecated version of the widget, ``jsoneditor`` - you can `see the differences here <https://github.com/josdejong/svelte-jsoneditor#differences-between-josdejongsvelte-jsoneditor-and-josdejongjsoneditor>`_.

You can read about why this isn't a part of the ``django-jsoneditor`` project `here <https://github.com/nnseva/django-jsoneditor/issues/71>`_, although it's our preference that the two projects merge in the future to avoid fragmentation.


Contents
========

.. toctree::
   :maxdepth: 2

   getting_started
   editor_properties
   settings
   contributing
   license
   version_history


Thanks
======

This project is heavily inspired by `Vsevolod Novikov's django-jsoneditor package <https://github.com/nnseva/django-jsoneditor>`_. Thanks @nnseva!
