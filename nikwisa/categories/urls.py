from django.urls import path
from rest_framework.routers import DefaultRouter
from categories.views import (
    CategoryViewSet,
    SubCategoryViewSet,
)

# Using DefaultRouter for a clean REST API approach
router = DefaultRouter()
router.register("", CategoryViewSet, basename="category")
router.register("subcategories", SubCategoryViewSet, basename="subcategory")

urlpatterns = router.urls
