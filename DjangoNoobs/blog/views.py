"""
Views functions for Blog application
"""


from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.shortcuts import get_object_or_404
from django.template.context_processors import csrf
from django.template.loader import render_to_string
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Tag, Category, Post, Comment
from .forms import TagForm, CategoryForm, PostForm, CommentForm
from .utils import ObjectDetailMixin, ObjectCreateMixin, ObjectUpdateMixin
from .utils import ObjectDeleteMixin, ObjectListMixin, LikeDislikeMixin


class PostList(ObjectListMixin, View):
    """
    This class-view used for return page with list of posts
    Using ObjectListMixin
    """
    model = Post
    template = 'blog/post_list.html'
    paginate_items = 10


class PostCreate(LoginRequiredMixin, ObjectCreateMixin, View):
    """
    This class-view used for return create post page
    Using ObjectCreateMixin and LoginRequiredMixin (from django-auth)
    """
    form_model = PostForm
    template = 'blog/post_create.html'
    raise_exception = True


class PostUpdate(LoginRequiredMixin, ObjectUpdateMixin, View):
    """
    This class-view used for return post update page
    Using ObjectUpdateMixin and LoginRequiredMixin (from django-auth)
    """
    model = Post
    form_model = PostForm
    template = 'blog/post_update.html'
    raise_exception = True


class PostDelete(LoginRequiredMixin, ObjectDeleteMixin, View):
    """
    This class-view used for return post delete page
    Using ObjectDeleteMixin and LoginRequiredMixin (from django-auth)
    """
    model = Post
    template = 'blog/includes/post_delete_dialog.html'
    redirect_url = 'posts_list_url'
    raise_exception = True


class TagList(ObjectListMixin, View):
    """
    This class-view used for return page with list of tags
    Using ObjectListMixin
    """
    model = Tag
    template = 'blog/tags_list.html'
    paginate_items = 100


class TagDetails(ObjectDetailMixin, View):
    """
    This class-view used for return page with details information about tag
    Using ObjectDetailMixin
    """
    model = Tag
    template = 'blog/tag_detail.html'


class TagCreate(LoginRequiredMixin, ObjectCreateMixin, View):
    """
    This class-view used for return create tag page
    Using ObjectCreateMixin and LoginRequiredMixin (from django-auth)
    """
    form_model = TagForm
    template = 'blog/tag_create.html'
    raise_exception = True


class TagUpdate(LoginRequiredMixin, ObjectUpdateMixin, View):
    """
    This class-view used for return tag update page
    Using ObjectUpdateMixin and LoginRequiredMixin (from django-auth)
    """
    model = Tag
    form_model = TagForm
    template = 'blog/tag_update.html'
    raise_exception = True


class TagDelete(LoginRequiredMixin, ObjectDeleteMixin, View):
    """
    This class-view used for return tag delete page
    Using ObjectDeleteMixin and LoginRequiredMixin (from django-auth)
    """
    model = Tag
    template = 'blog/includes/tag_delete_dialog.html'
    redirect_url = 'tags_list_url'
    raise_exception = True


class CategoryList(ObjectListMixin, View):
    """
    This class-view used for return page with list of categories
    Using ObjectListMixin
    """
    model = Category
    template = 'blog/category_list.html'
    paginate_items = 100


class CategoryDetails(ObjectDetailMixin, View):
    """
    This class-view used for return page with details information about categories
    Using ObjectDetailMixin
    """
    model = Category
    template = 'blog/category_detail.html'


class CategoryCreate(LoginRequiredMixin, ObjectCreateMixin, View):
    """
    This class-view used for return create category page
    Using ObjectCreateMixin and LoginRequiredMixin (from django-auth)
    """
    form_model = CategoryForm
    template = 'blog/category_create.html'
    raise_exception = True


class CategoryUpdate(LoginRequiredMixin, ObjectUpdateMixin, View):
    """
    This class-view used for return category update page
    Using ObjectUpdateMixin and LoginRequiredMixin (from django-auth)
    """
    model = Category
    form_model = CategoryForm
    template = 'blog/category_update.html'
    raise_exception = True


class CategoryDelete(LoginRequiredMixin, ObjectDeleteMixin, View):
    """
    This class-view used for return category delete page
    Using ObjectDeleteMixin and LoginRequiredMixin (from django-auth)
    """
    model = Category
    template = 'blog/includes/category_delete_dialog.html'
    redirect_url = 'category_list_url'
    raise_exception = True


class PostDetail(View):
    """
    This class-view used for return page with details
    information about post with comments
    """
    template = 'blog/post_detail.html'
    comment_form = CommentForm

    def get(self, request, slug, *args, **kwargs):
        """
        GET method for post page
        :param request: get user from request
        :param slug: slug of post
        :param args: args
        :param kwargs: kwargs
        :return: render template
        """
        post = get_object_or_404(Post, slug__iexact=slug)
        context = {}
        context.update(csrf(request))
        user = request.user
        context['post'] = post
        context['comments'] = post.comment_set.all().order_by('path')
        context['admin_object'] = post

        if user.is_authenticated:
            context['form'] = self.comment_form

        return render(request, self.template, context=context)


class LikePost(LoginRequiredMixin, LikeDislikeMixin, View):
    """
    This class-view used for like posts
    Using LikeDislikeMixin and LoginRequiredMixin (from django-auth)
    """
    model = Post
    get_model = 'post_id'
    type = 'likes'
    template = 'blog/includes/like_post.html'


class DislikePost(LoginRequiredMixin, LikeDislikeMixin, View):
    """
    This class-view used for dislike posts
    Using LikeDislikeMixin and LoginRequiredMixin (from django-auth)
    """
    model = Post
    get_model = 'post_id'
    type = 'dislikes'
    template = 'blog/includes/like_post.html'


class LikeComment(LoginRequiredMixin, LikeDislikeMixin, View):
    """
    This class-view used for like comments
    Using LikeDislikeMixin and LoginRequiredMixin (from django-auth)
    """
    model = Comment
    get_model = 'comment_id'
    type = 'likes'
    template = 'blog/includes/like_comment.html'


class DislikeComment(LoginRequiredMixin, LikeDislikeMixin, View):
    """
    This class-view used for dislike comments
    Using LikeDislikeMixin and LoginRequiredMixin (from django-auth)
    """
    model = Comment
    get_model = 'comment_id'
    type = 'dislikes'
    template = 'blog/includes/like_comment.html'


class AddComment(LoginRequiredMixin, View):
    """
    This class-view used for add comments
    Using LoginRequiredMixin (from django-auth)
    """
    def post(self, request, slug):
        """
        GET method for add comment page
        :param request: get form from request
        :param slug: slug of post
        :return: redirect to post page
        """
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

