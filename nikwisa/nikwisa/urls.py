from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include

# urlpatterns = [
#     path("admin/", admin.site.urls),
#     path("api/v1/test/", include("api.urls")),
# ]

urlpatterns = [
    path("api/v1/weddings/", include("weddings.urls")),
    path("api/v1/categories/", include("categories.urls")),
    path("admin/", admin.site.urls),
]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)