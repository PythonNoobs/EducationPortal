from django.db import models
from json import loads

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
    category_name = models.ForeignKey(QuizCategories, on_delete=models.SET_DEFAULT, default=None)

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
    question_type = models.CharField(max_length=20, null=True, choices=QUESTION_TYPES, default='Single Answer')
    question_points = models.IntegerField(null=False, default=1)
    linked_quiz = models.ForeignKey(Quiz, on_delete=models.PROTECT, null=False)

    class Meta:
        verbose_name_plural = 'Quiz questions'
        ordering = ['linked_quiz']

    def __str__(self):
        if len(self.question_text)>30:
            return f'{str(self.question_text)[:30]}... ({self.linked_quiz})'
        else:
            return f'{str(self.question_text)[:30]} ({self.linked_quiz})'

class QuizAnswers(models.Model):
    """
    Class for define answers for question(s)
    Linked to Quiz Question model
    """
    answers_dict = models.TextField(null=False)
    linked_question = models.ForeignKey(QuizQuestion, on_delete=models.PROTECT, null=False)

    class Meta:
        verbose_name_plural = 'Quiz answers'
        ordering = ['linked_question']

    def get_number_of_answers(self):
        return len(loads(self.answers_dict))

    def __str__(self):
        return f'{self.linked_question} ({self.get_number_of_answers()})'

    # TODO: Need to overwrite save method with additional check for dictionary format. 

class ActiveQuiz(models.Model):
    """
    Class for define status of quiz
    Linked to Quiz Question model
    """
    name = models.CharField(max_length=50, null=False)
    category_name = models.CharField(max_length=50, null=False)
    question = models.ForeignKey(QuizQuestion, on_delete=models.SET_DEFAULT, default=None) 
    question_done_flag = models.BooleanField(null=True)
    correct_answer_flag = models.BooleanField(null=True)
    started_at = models.DateTimeField(auto_now_add=True)
    finished_at = models.DateTimeField()
