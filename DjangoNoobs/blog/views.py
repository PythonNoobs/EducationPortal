# from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Post


class MainBlogPostList(ListView):
    model = Post
    paginate_by = 10
