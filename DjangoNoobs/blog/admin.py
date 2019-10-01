from django.contrib import admin
from .models import Post, Comment, Mark, Category, Tag

# Register your models here.
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Mark)
admin.site.register(Category)
admin.site.register(Tag)
