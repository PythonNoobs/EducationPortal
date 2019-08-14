from django.shortcuts import render, get_object_or_404, HttpResponse
from .models import Quiz, QuizQuestion, ActiveQuiz

def quiz_view(request):

    quiz_list = [item for item in Quiz.objects.all()]
    page_content = {'quiz_list': quiz_list}

    return render(request, 'testsystem/test_index.html', context=page_content)


# TODO: Need add check for existing IDs
def quiz_details(request, quiz_id, quiz_name, category_name):

    if request.method == 'GET':
        questions_id_list = [item.id for item in QuizQuestion.objects.filter(linked_quiz=quiz_id)]

        active_quiz_key = ActiveQuiz.store_active_quiz_data(questions_id_list, quiz_name, category_name)
    
        questions_list = [q for q in ActiveQuiz.objects.filter(active_quiz_key=active_quiz_key)]

        page_content = {'quiz_name': quiz_name,
            'active_quiz_questions': questions_list}

    return render(request, 'testsystem/questions.html', context=page_content)
