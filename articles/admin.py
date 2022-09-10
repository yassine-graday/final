from django.contrib import admin
from articles.models import Tag, Article

class TagAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Tag._meta.fields]


class ArticleAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Article._meta.fields]
    filter_horizontal=("tags",)
    

admin.site.register(Article, ArticleAdmin)
admin.site.register(Tag, TagAdmin)

# Register your models here.
