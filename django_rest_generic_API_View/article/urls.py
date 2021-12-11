from django.urls import path

from .views import ArticleView, SingleAcrticleView

app_name = "articles"

urlpatterns = [
    path('articles/', ArticleView.as_view()),
    path('articles/<int:pk>', SingleAcrticleView.as_view())
]
