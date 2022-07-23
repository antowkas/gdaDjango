from django.db import models


# Create your models here.
class Article(models.Model):
    heading = models.CharField(max_length=100, verbose_name="Заголовок")
    text = models.TextField(verbose_name="Текст")
    slug = models.SlugField(verbose_name="ЧПУ", blank=True, null=True, unique=True)

    def __str__(self):
        return f"Статья \"{self.heading}\""

    def get_articles(self):
        return self.comment_article.all()


class Comment(models.Model):
    author = models.CharField(max_length=100, verbose_name="Автор")
    text = models.TextField(verbose_name="Текст")
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="comment_article", verbose_name="Статья")

    def __str__(self):
        return f"Комментарий от пользователя {self.author} к статье \"{self.article}\""
