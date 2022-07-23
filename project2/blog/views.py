from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Article


# Create your views here.
def all_articles(request):
    a = Article.objects.all()
    context = {
        "articles": a
    }
    return render(request, "all_articles.html", context)


def article_n(request, slug):
    article = get_object_or_404(Article, slug=slug)
    context = {
        "article": article,
        "comments": article.get_articles()
    }
    return render(request, 'article_n.html', context)


@login_required
def heading_filter(request):
    if request.method == "GET":
        heading = request.GET.get("heading")
        a = None
        if heading:
            a = Article.objects.filter(heading__contains=heading)
        context = {
            "articles": a,
            "heading": heading,
        }
    return render(request, "heading_filter.html", context=context)
