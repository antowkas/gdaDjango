from django.shortcuts import render
from django.http import HttpResponse
from .models import Article


# Create your views here.
def all_articles(request):
    a = Article.objects.all()
    context = {
        "articles": a
    }
    return render(request, "all_articles.html", context)


def article_n(request):
    i = int(request.path.split("/")[-1])
    article, = Article.objects.filter(id=i)
    context = {
        "article": article,
        "comments": article.get_articles()
    }
    return render(request, 'article_n.html', context)
