"""
Classes (Models) for Quiz application
"""
from django.db import models

QUESTION_TYPES = [('Single Answer', 'Single Answer'),
                  ('Multi Answer', 'Multi Answer'),
                  ('User Input', 'User Input')]


class QuizCategories(models.Model):
    """
    Class for define quiz category
    """
    category_name = models.CharField(max_length=50, unique=True)

    class Meta:
        verbose_name_plural = 'Quiz Categories'
        ordering = ['category_name']

    def __str__(self):
        return f'{self.category_name}'


class Quiz(models.Model):
    """
    Class for define high level of quiz structure
    Linked to CategoryQuiz model
    """
    name = models.CharField(max_length=50, null=False)
    description = models.CharField(max_length=300, null=False)
    category_name = models.ForeignKey(
        QuizCategories, on_delete=models.SET_DEFAULT, default=None)

    class Meta:
        verbose_name_plural = 'Quiz'
        ordering = ['category_name']

    def __str__(self):
        return f'{self.name} ({self.category_name})'


class QuizQuestion(models.Model):
    """
    Class for define question for quiz
    Linked to Quiz model
    """
    question_text = models.TextField(null=False)
    question_code = models.TextField(null=True, default='', blank=True)
    question_type = models.CharField(
        max_length=20, null=True, choices=QUESTION_TYPES, default='Single Answer')
    question_points = models.IntegerField(null=False, default=1)
    linked_quiz = models.ForeignKey(Quiz, on_delete=models.PROTECT, null=False)
    answers_dict = models.TextField(null=False, default='')

    class Meta:
        verbose_name_plural = 'Quiz questions'
        ordering = ['linked_quiz']

    def __str__(self):
        if len(self.question_text) > 30:
            return f'{str(self.question_text)[:30]}... ({self.linked_quiz})'
        return f'{str(self.question_text)[:30]} ({self.linked_quiz})'

# TODO: Need to overwrite save method with additional check for dictionary format.


class ActiveQuiz(models.Model):
    """
    Class for define status of quiz
    Linked to Quiz Question model
    """
    active_quiz_key = models.CharField(max_length=50, null=False)
    name = models.CharField(max_length=50, null=False, default=None)
    category = models.CharField(max_length=50, null=False, default=None)
    question = models.ForeignKey(
        QuizQuestion, on_delete=models.SET_DEFAULT, default=None)
    question_done_flag = models.BooleanField(null=True)
    correct_answer_flag = models.BooleanField(null=True)
    started_at = models.DateTimeField(auto_now_add=True)
    finished_at = models.DateTimeField(null=True, blank=True)
    result = models.IntegerField(default=0)

    @staticmethod
    def store_active_quiz_data(question_id_shuffled_list, quiz_name, category_name):
        """
        staticmethod for store active quiz data to database
        return: active quiz key
        """
        from uuid import uuid1
        from datetime import datetime
        import django.utils.timezone
        _id = uuid1()
        _start_time = datetime.now()

        for question_id in question_id_shuffled_list:
            temp_active_quiz = ActiveQuiz()
            temp_active_quiz.active_quiz_key = _id
            temp_active_quiz.name = quiz_name
            temp_active_quiz.category = category_name
            temp_active_quiz.question = QuizQuestion.objects.get(
                pk=question_id)
            temp_active_quiz.question_done_flag = False
            temp_active_quiz.started_at = django.utils.timezone.now()
            temp_active_quiz.finished_at = None
            temp_active_quiz.save()

        return _id
