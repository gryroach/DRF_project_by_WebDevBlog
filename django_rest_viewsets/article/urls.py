from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import ArticleViewSet


router = DefaultRouter()
router.register('articles', ArticleViewSet, basename='user')

urlpatterns = router.urls
