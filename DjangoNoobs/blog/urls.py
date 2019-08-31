from django.urls import path
from . import views


urlpatterns = [
    path('', views.MainBlogPostList.as_view(), name='blog'),
]
