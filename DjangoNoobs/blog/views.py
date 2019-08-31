# from django.shortcuts import render
from django.views.generic.list import ListView
from .models import BlogPost


class MainBlogPostList(ListView):
    model = BlogPost
    paginate_by = 10
    ordering = ['-date']
