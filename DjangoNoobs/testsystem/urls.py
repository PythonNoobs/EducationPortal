from django.urls import path
from .views import quiz_details, quiz_view


urlpatterns = [
    path('', quiz_view, name='test'),
    path('<int:quiz_id>/<str:quiz_name>/<str:category_name>', quiz_details, name='questions'),
]
