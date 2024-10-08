from rest_framework import serializers
from blog.models import Article, Comment


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = "__all__"


class CommentSerializer(serializers.ModelSerializer):
    article = ArticleSerializer()

    class Meta:
        model = Comment
        fields = "__all__"


class CommentSerializerPost(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"
