""" Views functions for Quiz application """
from random import random
from django.shortcuts import render, get_object_or_404, redirect
from django.utils.datastructures import MultiValueDictKeyError
from django.views.generic import View, ListView
from .models import Quiz, QuizQuestion, ActiveQuiz
from .quizengine import get_question_from_quiz, check_answer


### Views block

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
    template_name = 'testsystem/details.html'
    page_content = {}

    def get(self, request, quiz_id):
        """GET"""
        quiz = get_object_or_404(Quiz, pk=quiz_id)

        questions_id_list = [
            item.id for item in QuizQuestion.objects.filter(linked_quiz=quiz_id)]
        
        shuffled_questions_id_list = sorted(questions_id_list, key=lambda k: random())

        self.page_content['quiz_name'] = quiz.name
        self.page_content['quiz_category_name'] = quiz.category_name
        self.page_content['quiz_description'] = quiz.description

        self.page_content['active_quiz_key'] = ActiveQuiz.store_active_quiz_data(
            shuffled_questions_id_list,
            self.page_content['quiz_name'],
            self.page_content['quiz_description'])

        return render(request, self.template_name, context=self.page_content)


class ActiveQuizView(View):
    """ This class-view used for manage with active quiz """
    template_name = 'testsystem/active_quiz.html'
    page_content = {}

    @staticmethod
    def __clean_skip_flag(_active_quiz_key):
        """ internal private function change all 'skip_flag' values to 'False'

        :param _active_quiz_key: (str) id key of action quiz

        :return: (list) list with ActiveQuiz objects
        """
        questions = [q for q in ActiveQuiz.objects.filter(
            active_quiz_key=_active_quiz_key) if q.skip_flag]
        for question in questions:
            question.skip_flag = False
            question.save()

    @staticmethod
    def __get_active_questions(_active_quiz_key):
        """ internal private function for get actual quiz

        :param _active_quiz_key: (str) id key of action quiz

        :raises: NoMoreQuestions, AllQuestionsSkipped, StopQuiz

        :return: (list) list with ActiveQuiz objects
        """

        questions_list_not_done = [q for q in ActiveQuiz.objects.filter(
            active_quiz_key=_active_quiz_key) if not q.question_done_flag]
        if not questions_list_not_done:
            raise NoMoreQuestions('Exception raised: No more questions!!!')

        questions_list_not_skipped = [
            q for q in questions_list_not_done if not q.skip_flag]
        if not questions_list_not_skipped:
            raise AllQuestionsSkipped(
                'Exception raised: Only skipped question(s) remained')

        final_questions_list = questions_list_not_skipped
        
        if not final_questions_list:
            raise StopQuiz('Exception raised: Quiz Finished !!!')

        return final_questions_list

    def get(self, request, active_quiz_key):
        """ GET """
        active_question_list = ActiveQuizView.__get_active_questions(
            active_quiz_key)
        active_question = active_question_list.pop()
        self.page_content['active_quiz_key'] = active_quiz_key
        self.page_content['active_question'] = active_question
        self.page_content['answers'] = active_question.question.answers_dict.keys()

        return render(request, self.template_name, context=self.page_content)

    def post(self, request, active_quiz_key):
        """ POST """
        _action = request.POST['id_action']
        question_id = request.POST['id_question']
        answer_id = None

        try:
            answer_id = request.POST['answerOption']
        except MultiValueDictKeyError:
            _action = 'SKIP'

        if _action == 'SKIP':
            temp_act_quiz_obj = get_question_from_quiz(active_quiz_key, question_id)
            temp_act_quiz_obj.skip_flag = True
            temp_act_quiz_obj.save()

        if _action == 'SUBMIT':
            temp_act_quiz_obj = get_question_from_quiz(active_quiz_key, question_id)
            temp_act_quiz_obj.correct_answer_flag = check_answer(temp_act_quiz_obj, answer_id)
            temp_act_quiz_obj.question_done_flag = True
            temp_act_quiz_obj.save()

        try:
            active_question_list = ActiveQuizView.__get_active_questions(
                active_quiz_key)
        except NoMoreQuestions:
            return redirect('result_page', active_quiz_key)
        except AllQuestionsSkipped:
            ActiveQuizView.__clean_skip_flag(active_quiz_key)
            active_question_list = ActiveQuizView.__get_active_questions(
                active_quiz_key)
        except StopQuiz:
            return redirect('result_page', active_quiz_key)

        active_question = active_question_list.pop()
        self.page_content['active_quiz_key'] = active_quiz_key
        self.page_content['active_question'] = active_question
        self.page_content['answers'] = active_question.question.answers_dict.keys()


        return render(request, self.template_name, context=self.page_content)


def result_page_view(request, active_quiz_key):
    """ view function for return result page after quiz finished

    :param active_quiz_key: (str) id key of action quiz

    :return: HttpResponse with 'testsystem/result_page.html' and 'page_content'
    """
    page_content = {}
    page_content['quiz_results'] = ActiveQuiz.objects.filter(
        active_quiz_key=active_quiz_key)
    return render(request, 'testsystem/result_page.html', context=page_content)


### Exceptions Block

class NoMoreQuestions(Exception):
    """
    exception signal about empty question list
    """
    def __init__(self, message):
        super(NoMoreQuestions, self).__init__(message)
        self.message = message


class AllQuestionsSkipped(Exception):
    """
    exception signal about anly skipped question is in question list
    """
    def __init__(self, message):
        super(AllQuestionsSkipped, self).__init__(message)
        self.message = message


class StopQuiz(Exception):
    """
    exception signal about stop the quiz
    """
    def __init__(self, message):
        super(StopQuiz, self).__init__(message)
        self.message = message
