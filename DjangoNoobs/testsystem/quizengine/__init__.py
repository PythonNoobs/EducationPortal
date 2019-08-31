""" Quiz back-end engine

    Used for manipulation with active quiz (calculating points, results, ect)
"""
from testsystem.models import ActiveQuiz, HistoryQuiz


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


def store_quiz_to_history(active_quiz_key):
    """ storing active quiz to the history quiz table
    and deletes it from active quiz table

    :param active_quiz_key: (str) id key of action quiz

    :return:
    """
    active_quiz_list = [item for item in ActiveQuiz.objects.filter(
        active_quiz_key=active_quiz_key)]

    for item in active_quiz_list:
        temp_history_item = HistoryQuiz()
        temp_history_item.active_quiz_key = item.active_quiz_key
        temp_history_item.name = item.name
        temp_history_item.category = item.category
        temp_history_item.question = item.question.question_text
        temp_history_item.correct_answer_flag = item.correct_answer_flag
        temp_history_item.finished_at = item.finished_at
        temp_history_item.result = item.result
        temp_history_item.save()

    ActiveQuiz.objects.filter(active_quiz_key=active_quiz_key).delete()

    return HistoryQuiz.objects.filter(active_quiz_key=active_quiz_key)
