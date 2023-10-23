from django.contrib import admin
from django.urls import include, re_path
from django.views.generic.base import RedirectView


admin.autodiscover()


urlpatterns = [
    # Include the django admin so we can use it with the example app
    re_path(r"^admin/", admin.site.urls),
    # Add hte debug toolbar in case it's helpful developing the widget
    re_path(r"^__debug__/", include("debug_toolbar.urls")),
    # Redirect to the admin for convenience when using the example app :)
    re_path(r"^", RedirectView.as_view(url="admin/")),
]
