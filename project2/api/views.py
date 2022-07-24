from rest_framework import viewsets

from blog.models import Article, Comment
from .serializers import ArticleSerializer, CommentSerializer, CommentSerializerPost


class ArticleViewset(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class CommentViewset(viewsets.ModelViewSet):
    queryset = Comment.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CommentSerializerPost
        return CommentSerializer
