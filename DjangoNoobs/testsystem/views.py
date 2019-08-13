from django.shortcuts import render, get_object_or_404, HttpResponse
from .models import Quiz, QuizQuestion

def quiz_view(request):

    quiz_list = [item for item in Quiz.objects.all()]
    page_content = {'quiz_list': quiz_list}

    return render(request, 'testsystem/test_index.html', context=page_content)


# TODO: Need add check for existing IDs
def quiz_details(request, quiz_id):

    if request.method == 'GET':
        questions_list = [item for item in QuizQuestion.objects.filter(linked_quiz=quiz_id)]
        page_content = {'questions_list': questions_list}

    return render(request, 'testsystem/questions.html', context=page_content)
