from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import ArticleViewset, CommentViewset

urlpatterns = [
]

router = DefaultRouter()

router.register('articles', ArticleViewset)
router.register('comments', CommentViewset)

urlpatterns += router.urls
