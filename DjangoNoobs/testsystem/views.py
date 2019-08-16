"""
Views functions for Quiz application
"""
from django.shortcuts import render
from .models import Quiz, QuizQuestion, ActiveQuiz


def quiz_view(request):
    """
    This view function return start page for Quiz application
    """
    quiz_list = [item for item in Quiz.objects.all()]
    page_content = {'quiz_list': quiz_list}

    return render(request, 'testsystem/test_index.html', context=page_content)

# TODO: Need add check for existing IDs


def quiz_details(request, quiz_id):
    """
    This view function return page with Quiz descriptions
    and creates ActiveQuiz table in database
    """
    if request.method == 'GET':
        questions_id_list = [
            item.id for item in QuizQuestion.objects.filter(linked_quiz=quiz_id)]

        quiz = Quiz.objects.get(pk=quiz_id)

        quiz_name = quiz.name
        quiz_category_name = quiz.category_name
        quiz_description = quiz.description

        active_quiz_key = ActiveQuiz.store_active_quiz_data(questions_id_list,
                                                            quiz_name,
                                                            quiz_description)

        page_content = {'quiz_name': quiz_name,
                        'quiz_category_name': quiz_category_name,
                        'quiz_description': quiz_description,
                        'active_quiz_key': active_quiz_key}

    return render(request, 'testsystem/details.html', context=page_content)


def active_quiz(request, active_quiz_key):
    """
    This view function return active quiz page and starts quiz engine
    """
    page_content = {'active_quiz_key': active_quiz_key}

    return render(request, 'testsystem/active_quiz.html', context=page_content)
