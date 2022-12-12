from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import ProductViewSet

router = DefaultRouter()
router.register(r'items', ProductViewSet, basename='item')

urlpatterns = [
    path('v1/', include(router.urls))
]
