from django.conf import settings


CONFIG_DEFAULTS = {
    "PROPS": {
        "mode": "tree",
        "mainMenuBar": True,
        "navigationBar": True,
        "statusBar": True,
        "askToFormat": True,
        "readOnly": False,
        "indentations": 4,
        "tabSize": 4,
        "escapeControlCharacters": False,
        "flattenColumns": True,
    }
}


def get_config():
    return {
        "PROPS": {
            **CONFIG_DEFAULTS["PROPS"],
            **getattr(settings, "SVELTE_JSONEDITOR", {}).get("PROPS", {}),
        }
    }
