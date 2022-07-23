from django.urls import path, re_path
from .views import all_articles, article_n, heading_filter


app_name = "blog"


urlpatterns = [
    path("all_articles/", all_articles, name="all_articles"),
    path("article/<slug>", article_n),
    path("heading_filter/", heading_filter, name="heading_filter"),

]
