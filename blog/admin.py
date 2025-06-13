from django.contrib import admin
from .models import Post, Comment, Categoria

admin.site.register(Categoria)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'data_criacao')
    search_fields = ('titulo', 'conteudo')
    list_filter = ('data_criacao',)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'autor', 'data_criacao')
    search_fields = ('conteudo',)
    list_filter = ('data_criacao',)
