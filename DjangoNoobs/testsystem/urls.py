"""
urls for test system application
"""
from django.urls import path
from . import views


urlpatterns = [
    path('', views.QuizView.as_view(), name='test'),
    path('add_question_page', views.AddQuestionView.as_view(), name='add_question'),
    path('<int:quiz_id>', views.QuizDetailsView.as_view(), name='quiz_details'),
    path('<str:active_quiz_key>', views.ActiveQuizView.as_view(), name='active_quiz'),
    path('result/<str:active_quiz_key>', views.result_page_view, name='result_page'),

]
