"""
Urls patterns for blog application
"""


from django.urls import path
from .views import *


urlpatterns = [
    # path('', posts_list, name='posts_list_url'),
    path('', PostList.as_view(), name='posts_list_url'),
    path('post/create/', PostCreate.as_view(), name='post_create_url'),
    # path('post/<str:slug>/', PostDetail.as_view(), name='post_detail_url'),  # don't delete this
    path('post/<str:slug>/update/', PostUpdate.as_view(), name='post_update_url'),
    path('post/<str:slug>/delete/', PostDelete.as_view(), name='post_delete_url'),

    # path('tags/', tags_list, name='tags_list_url'),
    path('tags/', TagList.as_view(), name='tags_list_url'),
    path('tags/create/', TagCreate.as_view(), name='tag_create_url'),
    path('tags/<str:slug>/', TagDetails.as_view(), name='tag_detail_url'),
    path('tags/<str:slug>/update/', TagUpdate.as_view(), name='tag_update_url'),
    path('tags/<str:slug>/delete/', TagDelete.as_view(), name='tag_delete_url'),

    # path('category/', category_list, name='category_list_url'),
    path('category/', CategoryList.as_view(), name='category_list_url'),
    path('category/create/', CategoryCreate.as_view(), name='category_create_url'),
    path('category/<str:slug>/', CategoryDetails.as_view(), name='category_detail_url'),
    path('category/<str:slug>/update/', CategoryUpdate.as_view(), name='category_update_url'),
    path('category/<str:slug>/delete/', CategoryDelete.as_view(), name='category_delete_url'),

    # For comments (TEST ROUT)
    path('post/<str:slug>/', PostDetail.as_view(), name='post_detail_url'),
    path('post/<str:slug>/comment/', add_comment, name='post_comment_url'),

    # For likes
    path('post_like/', LikePost.as_view(), name='like_post'),
    path('post_dislike/', DislikePost.as_view(), name='dislike_post'),
    path('comment_like/', LikeComment.as_view(), name='like_comment'),
    path('comment_dislike/', DislikeComment.as_view(), name='dislike_comment'),
]
