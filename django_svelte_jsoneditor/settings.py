from django.conf import settings

from .exceptions import InvalidPropError


DEFAULT_SVELTE_JSONEDITOR_PROPS = {
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


_AVAILABLE_PROPS = set(DEFAULT_SVELTE_JSONEDITOR_PROPS.keys())


def check_props(props):
    """Check that props given to the widget are valid"""
    for key in props:
        if key not in _AVAILABLE_PROPS:
            raise InvalidPropError(f"Invalid prop '{key}'")

    return props


def get_props():
    """Get default props overridden by any props set in the SVELTE_JSONEDITOR_PROPS setting"""
    return check_props(
        {
            **DEFAULT_SVELTE_JSONEDITOR_PROPS,
            **getattr(settings, "SVELTE_JSONEDITOR_PROPS", {}),
        }
    )
