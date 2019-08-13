from django.urls import path
from .views import quiz_details, quiz_view


urlpatterns = [
    path('', quiz_view, name='test'),
    path('quiz/<int:quiz_id>/', quiz_details, name='questions'),
]
