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


def check_answer(active_question, answer_id_list):
    """ checking answer for correct or not
    :param active_question: (ActiveQuiz)

    :param answer_id_list: (string) list of ids of current answer

    :return: (boolean)
    """
    _question_type = active_question.question.question_type
    _answers_dict = active_question.question.answers_dict
    _question_check_sum = sum(active_question.question.answers_dict.values())
    _answers_check_sum = 0

    if _question_type == 'Single Answer':
        if _answers_dict[answer_id_list[0]] == 1:
            return True

    elif _question_type == 'Multi Answer':
        for answer in answer_id_list:
            if _answers_dict[answer] == 1:
                _answers_check_sum = _answers_check_sum + 1

            if _answers_dict[answer] == 0:
                return False
                
        if _answers_check_sum == _question_check_sum:
            return True
    return False


def store_quiz_to_history(active_quiz_key, _user_inctance=None):
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
        temp_history_item.user_id = _user_inctance
        temp_history_item.save()

    ActiveQuiz.objects.filter(active_quiz_key=active_quiz_key).delete()

    return HistoryQuiz.objects.filter(active_quiz_key=active_quiz_key)


def get_result_quiz_points(active_quiz_key):
    """ returns sum of points for finished quiz (from History table)

    :param active_quiz_key: active_quiz_key: (str) id key of action quiz
    :return:
    """
    history_quiz = HistoryQuiz.objects.filter(active_quiz_key=active_quiz_key)
    points_list = [p.result for p in history_quiz]
    points_summary = sum(points_list)

    return points_summary
