# Disables for testing:
# pylint: disable=missing-docstring
# pylint: disable=protected-access
# pylint: disable=too-many-public-methods


from django.urls import reverse


def get_admin_add_view_url(cls):
    """Get a url for model class instance add view in the admin
    Provide a Model subclass.
    """
    obj = cls()
    return reverse(f"admin:{obj._meta.app_label}_{type(obj).__name__.lower()}_add")


def get_admin_change_view_url(obj):
    """Get a url for an object's change view in the admin"""
    return reverse(f"admin:{obj._meta.app_label}_{type(obj).__name__.lower()}_change", args=(obj.pk,))
