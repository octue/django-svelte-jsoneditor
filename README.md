[![PyPI version](https://badge.fury.io/py/django-svelte-jsoneditor.svg)](https://badge.fury.io/py/django-svelte-jsoneditor)
[![Documentation Status](https://readthedocs.org/projects/django-svelte-jsoneditor/badge/?version=latest)](https://django-svelte-jsoneditor.readthedocs.io/en/latest/?badge=latest)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)

# django-svelte-jsoneditor

A plug in widget for django's JSONField that allows manipulation and display of JSON data. The widget is built using Jos deJong's new [svelte-jsoneditor](https://github.com/josdejong/svelte-jsoneditor).

This app is a replacement for `django-jsoneditor` (which uses a deprecated version of the widget, `jsoneditor` - you can [see the differences here](https://github.com/josdejong/svelte-jsoneditor#differences-between-josdejongsvelte-jsoneditor-and-josdejongjsoneditor)). You can read about why we're not directly contributing to `django-jsoneditor` [here](https://github.com/nnseva/django-jsoneditor/issues/71), the two projects might merge in the future.

## Documentation...

(working on it)

## About Svelte

**You don't need to know or care.** It's the JavaScript framework used to develop the widget - but the widget JS is all pre-built so there are no extra requirements.

### Developing

To get started with developing `django-svelte-jsoneditor`, fork the repo then open an environment in the devcontainer (the easiest way is to use GitHub codespaces or VSCode remote containers), then type:

```
python manage.py migrate
python manage.py createsuperuser
# (then enter user details for yourself)
python manage.py runserver
# (then go to the localhost address in your browser)
# (and in another terminal...)
pytest
# (this should run all tests and have them pass)
```

You'll find this takes you to the django admin where you have several example models registered, each of which use slightly different options on the json field, so you can see how the widget behaves.
