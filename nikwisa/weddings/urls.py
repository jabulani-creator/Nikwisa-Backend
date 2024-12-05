# weddings/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import WeddingViewSet

router = DefaultRouter()
router.register(r'weddings', WeddingViewSet)

urlpatterns = [
    path('', include(router.urls)),
]


# from django.urls import path
# from rest_framework.routers import DefaultRouter
# from weddings.views import (
#     WeddingsCategoryViewSet,
#     WeddingSubCategoryViewSet,
#     WeddingsViewSet
# )

# # Using DefaultRouter for a clean REST API approach
# router = DefaultRouter()
# router.register("categories", WeddingsCategoryViewSet, basename="weddings-category")
# router.register("subcategories", WeddingSubCategoryViewSet, basename="weddings-subcategory")
# router.register("", WeddingsViewSet, basename="weddings")

# urlpatterns = router.urls
