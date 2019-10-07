"""
Urls patterns for blog application
"""


from django.urls import path
from .views import PostList, PostCreate, PostUpdate, PostDelete, TagList, TagCreate
from .views import TagDetails, TagUpdate, TagDelete, CategoryList, CategoryCreate
from .views import CategoryDetails, CategoryUpdate, CategoryDelete, PostDetail
from .views import LikePost, DislikePost, LikeComment, DislikeComment, AddComment


urlpatterns = [
    # urls for posts
    path('', PostList.as_view(), name='posts_list_url'),
    path('post/create/', PostCreate.as_view(), name='post_create_url'),
    path('post/<str:slug>/', PostDetail.as_view(), name='post_detail_url'),
    path('post/<str:slug>/update/', PostUpdate.as_view(), name='post_update_url'),
    path('post/<str:slug>/delete/', PostDelete.as_view(), name='post_delete_url'),

    # urls for tags
    path('tags/', TagList.as_view(), name='tags_list_url'),
    path('tags/create/', TagCreate.as_view(), name='tag_create_url'),
    path('tags/<str:slug>/', TagDetails.as_view(), name='tag_detail_url'),
    path('tags/<str:slug>/update/', TagUpdate.as_view(), name='tag_update_url'),
    path('tags/<str:slug>/delete/', TagDelete.as_view(), name='tag_delete_url'),

    # urls for categories
    path('category/', CategoryList.as_view(), name='category_list_url'),
    path('category/create/', CategoryCreate.as_view(), name='category_create_url'),
    path('category/<str:slug>/', CategoryDetails.as_view(), name='category_detail_url'),
    path('category/<str:slug>/update/', CategoryUpdate.as_view(), name='category_update_url'),
    path('category/<str:slug>/delete/', CategoryDelete.as_view(), name='category_delete_url'),

    # urls for comments
    path('post/<str:slug>/comment/', AddComment.as_view(), name='post_comment_url'),

    # urls for likes
    path('post_like/', LikePost.as_view(), name='like_post'),
    path('post_dislike/', DislikePost.as_view(), name='dislike_post'),
    path('comment_like/', LikeComment.as_view(), name='like_comment'),
    path('comment_dislike/', DislikeComment.as_view(), name='dislike_comment'),
]
