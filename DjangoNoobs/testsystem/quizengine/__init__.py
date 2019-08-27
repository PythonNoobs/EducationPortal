""" Quiz back-end engine

    Used for manipulation with active quiz (calculating points, results, ect)
"""
from testsystem.models import ActiveQuiz

def get_question_from_quiz(active_quiz_key, question_id):

    """ return ActiveQuiz object (1 single question)
    :param active_quiz_key: (str) id key of action quiz

    :param question_id: (int) id of current question

    :return: QuerySet with ActiveQuiz object
    """
    return ActiveQuiz.objects.get(
        active_quiz_key=active_quiz_key, question=question_id)

def check_answer(active_question, answer_id):

    """ checking answer for correct or not
    :param active_question: (ActiveQuiz)

    :param answer_id: (string) id of current answer

    :return: (boolean)
    """
    if active_question.question.answers_dict[answer_id] == 1:
        return True
    return False
