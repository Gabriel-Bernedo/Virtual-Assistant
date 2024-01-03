from django.contrib import admin
from django.urls import path, include

from .views.viewsets import InfoViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'learn', InfoViewSet, basename='learn')
urlpatterns = router.urls

urlpatterns += [
]