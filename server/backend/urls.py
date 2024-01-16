from django.contrib import admin
from django.urls import path, include

from .views.viewsets import InfoViewSet, QuestionViewSet, SubjectViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'learn', InfoViewSet, basename='learn')
router.register(r'quiz', QuestionViewSet, basename='quiz')
router.register(r'subs', SubjectViewSet, basename='subs')

urlpatterns = router.urls

urlpatterns += [
]