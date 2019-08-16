from django.urls import path
from . import views 


urlpatterns = [
    path('', views.quiz_view, name='test'),
    path('<int:quiz_id>', views.quiz_details, name='quiz_details'),
    path('<str:active_quiz_key>', views.active_quiz, name='active_quiz')
]
