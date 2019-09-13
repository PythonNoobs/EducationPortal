from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render_to_response, redirect
from django.shortcuts import get_object_or_404
from django.template.context_processors import csrf
from django.views.decorators.http import require_http_methods
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Tag
from .models import Category
from .models import Post
from .models import Comment
from .forms import CategoryForm
from .forms import PostForm
from .forms import TagForm
from .forms import CommentForm
from .utils import ObjectDetailMixin
from .utils import ObjectCreateMixin
from .utils import ObjectUpdateMixin
from .utils import ObjectDeleteMixin
from .utils import ObjectListMixin


class PostList(ObjectListMixin, View):
    model = Post
    template = 'blog/post_list.html'
    paginate_items = 10


# class PostDetail(ObjectDetailMixin, View):
#     model = Post
#     template = 'blog/post_detail.html'


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
    paginate_items = 100


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


class PostDetail(View):
    template = 'blog/post_detail.html'
    comment_form = CommentForm

    def get(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug__iexact=slug)
        context = {}
        context.update(csrf(request))
        user = auth.get_user(request)
        context['post'] = post
        context['comments'] = post.comment_set.all().order_by('path')
        context['next'] = post.get_absolute_url()
        context['detail'] = True
        context['admin_object'] = Post

        if user.is_authenticated:
            context['form'] = self.comment_form

        return render_to_response(template_name=self.template, context=context)


@login_required
@require_http_methods(["POST"])
def add_comment(request, slug):
    form = CommentForm(request.POST)
    post = get_object_or_404(Post, slug__iexact=slug)

    if form.is_valid():
        comment = Comment()
        comment.path = []
        comment.post_id = post
        comment.author_id = auth.get_user(request)
        comment.content = form.cleaned_data['comment_area']
        comment.save()
        try:
            comment.path.extend(Comment.objects.get(id=form.cleaned_data['parent_comment']).path)
            comment.path.append(comment.id)
        except ObjectDoesNotExist:
            comment.path.append(comment.id)
        comment.save()

    return redirect(post.get_absolute_url())