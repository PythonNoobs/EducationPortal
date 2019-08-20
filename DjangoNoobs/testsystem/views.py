"""
Views functions for Quiz application
"""
from django.shortcuts import render, get_object_or_404
from django.views.generic import View, ListView
from .models import Quiz, QuizQuestion, ActiveQuiz


class QuizView(ListView):
    """
    This class-view used for return start page for Quiz application
    with list of quiz-tests
    """
    model = Quiz


class QuizDetailsView(View):
    """
    This class-view used for manage with Quiz description
    and creates ActiveQuiz table in database
    """
    template_name = 'index.html'
    page_content = {}

    def get(self, request, quiz_id):
        """GET"""

        quiz = get_object_or_404(Quiz, pk=quiz_id)

        questions_id_list = [
            item.id for item in QuizQuestion.objects.filter(linked_quiz=quiz_id)]

        self.page_content['quiz_name'] = quiz.name
        self.page_content['quiz_category_name'] = quiz.category_name
        self.page_content['quiz_description'] = quiz.description

        self.page_content['active_quiz_key'] = ActiveQuiz.store_active_quiz_data(
            questions_id_list,
            self.page_content['quiz_name'],
            self.page_content['quiz_description'])

        return render(request, 'testsystem/details.html', context=self.page_content)

class ActiveQuizView(View):
    """
    This class-view used for manage with active quiz
    """
    template_name = 'testsystem/active_quiz.html'
    page_content = {}

    @staticmethod
    def _get_active_questions(_active_quiz_key):
        return [q for q in ActiveQuiz.objects.filter(active_quiz_key=_active_quiz_key) if not q.question_done_flag]

    def get(self, request, active_quiz_key):
        """GET"""
        active_question_list = ActiveQuizView._get_active_questions(active_quiz_key)
        active_question = active_question_list.pop()
        self.page_content['active_quiz_key'] = active_quiz_key
        self.page_content['active_question'] = active_question
        # self.page_content['answers'] = active_question.question.get_answers()
        self.page_content['answers'] = active_question.question.get_answers().keys()

        return render(request, self.template_name, context=self.page_content)

    def post(self, request, active_quiz_key):
        """POST"""
        active_question_list = ActiveQuizView._get_active_questions(active_quiz_key)
        active_question = active_question_list.pop()
        self.page_content['active_quiz_key'] = active_quiz_key
        self.page_content['active_question'] = active_question

        return render(request, self.template_name, context=self.page_content)
