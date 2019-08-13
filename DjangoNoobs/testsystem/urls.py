from django.urls import path
from .views import quiz_details, quiz_view


urlpatterns = [
    path('', quiz_view, name='test'),
    path('questions/', quiz_details, name='questions'),
]
