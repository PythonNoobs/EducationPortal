from django.shortcuts import render, redirect, reverse
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Tag, Category, Post
from .forms import CategoryForm
from .forms import PostForm
from .forms import TagForm
from .utils import ObjectDetailMixin
from .utils import ObjectCreateMixin
from .utils import ObjectUpdateMixin
from .utils import ObjectDeleteMixin
from .utils import ObjectListMixin


class PostList(ObjectListMixin, View):
    model = Post
    template = 'blog/post_list.html'
    paginate_items = 10


class PostDetail(ObjectDetailMixin, View):
    model = Post
    template = 'blog/post_detail.html'


class PostCreate(LoginRequiredMixin, ObjectCreateMixin, View):
    form_model = PostForm
    template = 'blog/post_create.html'
    raise_exception = True


class PostUpdate(LoginRequiredMixin, ObjectUpdateMixin, View):
    model = Post
    form_model = PostForm
    template = 'blog/post_update.html'
    raise_exception = True


class PostDelete(LoginRequiredMixin, ObjectDeleteMixin, View):
    model = Post
    template = 'blog/includes/post_delete_dialog.html'
    redirect_url = 'posts_list_url'
    raise_exception = True


class TagList(ObjectListMixin, View):
    model = Tag
    template = 'blog/tags_list.html'
    paginate_items = 100


class TagDetails(ObjectDetailMixin, View):
    model = Tag
    template = 'blog/tag_detail.html'


class TagCreate(LoginRequiredMixin, ObjectCreateMixin, View):
    form_model = TagForm
    template = 'blog/tag_create.html'
    raise_exception = True


class TagUpdate(LoginRequiredMixin, ObjectUpdateMixin, View):
    model = Tag
    form_model = TagForm
    template = 'blog/tag_update.html'
    raise_exception = True


class TagDelete(LoginRequiredMixin, ObjectDeleteMixin, View):
    model = Tag
    template = 'blog/includes/tag_delete_dialog.html'
    redirect_url = 'tags_list_url'
    raise_exception = True


class CategoryList(ObjectListMixin, View):
    model = Category
    template = 'blog/category_list.html'
    paginate_items = 10


class CategoryDetails(ObjectDetailMixin, View):
    model = Category
    template = 'blog/category_detail.html'


class CategoryCreate(LoginRequiredMixin, ObjectCreateMixin, View):
    form_model = CategoryForm
    template = 'blog/category_create.html'
    raise_exception = True


class CategoryUpdate(LoginRequiredMixin, ObjectUpdateMixin, View):
    model = Category
    form_model = CategoryForm
    template = 'blog/category_update.html'
    raise_exception = True


class CategoryDelete(LoginRequiredMixin, ObjectDeleteMixin, View):
    model = Category
    template = 'blog/includes/category_delete_dialog.html'
    redirect_url = 'category_list_url'
    raise_exception = True
