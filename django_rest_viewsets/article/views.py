from rest_framework.viewsets import ModelViewSet


from .models import Article, Author
from .serializers import ArticleSerializer


class ArticleViewSet(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
