"""
Views functions for Quiz application
"""
from django.shortcuts import render
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
        questions_id_list = [
            item.id for item in QuizQuestion.objects.filter(linked_quiz=quiz_id)]

        quiz = Quiz.objects.get(pk=quiz_id)

        self.page_content['quiz_name'] = quiz.name
        self.page_content['quiz_category_name'] = quiz.category_name
        self.page_content['quiz_description'] = quiz.description

        self.page_content['active_quiz_key'] = ActiveQuiz.store_active_quiz_data(
            questions_id_list,
            self.page_content['quiz_name'],
            self.page_content['quiz_description'])

        return render(request, 'testsystem/details.html', context=self.page_content)

# TODO: Need add check for existing IDs


class ActiveQuizView(View):
    """
    This class-view used for manage with active quiz
    """
    template_name = 'testsystem/active_quiz.html'
    page_content = {}

    def get(self, request, active_quiz_key):
        """GET"""
        # TODO: need to create sepatrate function for get actual question
        active_question_list = [q for q in ActiveQuiz.objects.filter(
            active_quiz_key=active_quiz_key) if not q.question_done_flag]

        active_question = active_question_list.pop()
        self.page_content['active_quiz_key'] = active_quiz_key
        self.page_content['active_question'] = active_question

        return render(request, self.template_name, context=self.page_content)

    def post(self, request, active_quiz_key):
        """POST"""
        # TODO: need to create sepatrate function for get actual question
        active_question_list = [q for q in ActiveQuiz.objects.filter(
            active_quiz_key=active_quiz_key) if not q.question_done_flag]

        active_question = active_question_list.pop()
        self.page_content['active_quiz_key'] = active_quiz_key
        self.page_content['active_question'] = active_question

        return render(request, self.template_name, context=self.page_content)
