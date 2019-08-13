from django.shortcuts import render, get_object_or_404, HttpResponse
from .models import Quiz, QuizQuestion, QuizAnswers

# Create your views here.
def quiz_view(request):

    quiz_data = [item for item in Quiz.objects.all()]
    page_content = {'quiz_data': quiz_data}

    return render(request, 'testsystem/test_index.html', context=page_content)


def quiz_details(request, quiz_id):
    quiz_questions = QuizQuestion.objects().filter(linked_quiz=quiz_id)
    print(quiz_questions)
    return render(request, 'testsystem/questions.html')