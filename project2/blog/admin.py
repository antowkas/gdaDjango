from django.contrib import admin
from .models import Article, Comment

# Register your models here.
admin.site.register(Comment)


class CommentAdminInline(admin.TabularInline):
    model = Comment
    fk_name = "article"
    extra = 1


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [CommentAdminInline]
    prepopulated_fields = {
        "slug": ('heading',)
    }