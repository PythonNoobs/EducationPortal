from django.shortcuts import render, redirect, reverse
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from .models import Tag, Category, Post
from .forms import TagForm, CategoryForm, PostForm
from .utils import ObjectDetailMixin, ObjectCreateMixin, ObjectUpdateMixin, ObjectDeleteMixin, ObjectListMixin


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

# для @DanInSpace
# нет необходимости использовать отдельный метод, возврат к миксину, автор устанавливается
# def post_create(request):
#     if request.method == "POST":
#         form = PostForm(request.POST)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.author = request.user
#             post.save()
#             post.slug = slugify(post.title + str(post.id))
#             list_tags = request.POST.getlist('tags')
#             post.tags.add(*list_tags)
#             post.save()
#             return redirect('/blog/post/' + str(post.slug))
#     else:
#         form = PostForm()
#         return render(request, 'blog/post_create.html', {'form': form})


class PostUpdate(LoginRequiredMixin, ObjectUpdateMixin, View):
    model = Post
    form_model = PostForm
    template = 'blog/post_update.html'
    raise_exception = True


class PostDelete(LoginRequiredMixin, ObjectDeleteMixin, View):
    model = Post
    template = 'blog/post_delete.html'
    redirect_url = 'posts_list_url'
    raise_exception = True


class TagList(ObjectListMixin, View):
    model = Tag
    template = 'blog/tags_list.html'
    paginate_items = 10


# Delete after check mixin
def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'blog/tags_list.html', context={'tags': tags})


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
    template = 'blog/tag_delete.html'
    redirect_url = 'tags_list_url'
    raise_exception = True


class CategoryList(ObjectListMixin, View):
    model = Category
    template = 'blog/category_list.html'
    paginate_items = 10


# Delete after check mixin
def category_list(request):
    categories = Category.objects.all()
    return render(request, 'blog/category_list.html', context={'categories': categories})


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
    template = 'blog/category_delete.html'
    redirect_url = 'category_list_url'
    raise_exception = True
