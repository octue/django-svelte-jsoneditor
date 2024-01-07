from django.conf import settings


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
    "flattenColumns": True,
}


def get_props():
    """Get default props overridden by any props set in the SVELTE_JSONEDITOR_PROPS setting"""
    return {
        **DEFAULT_SVELTE_JSONEDITOR_PROPS,
        **getattr(settings, "SVELTE_JSONEDITOR_PROPS", {}),
    }
