from django.urls import path, re_path
from .views import all_articles, article_n


urlpatterns = [
    path("all_articles/", all_articles),
    re_path(r"^article/[0-9]+", article_n)
]
