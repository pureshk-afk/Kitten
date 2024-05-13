from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, re_path
from django.views.static import serve

urlpatterns = [
    path("", include("app.urls")),
    path("admin/", admin.site.urls),
    re_path(
        r"^media/(?P<path>.*)$",
        serve,
        {
            "document_root": settings.MEDIA_ROOT,
        },
    ),
]

urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


handler404 = "app.handlers.not_found_handler"
handler500 = "app.handlers.server_error_handler"
