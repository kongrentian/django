from django.contrib import admin
from .models import Post, Author, PostCategory, Category, Comment

# Register your models here.
admin.site.register(Post)
admin.site.register(PostCategory)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Author)
