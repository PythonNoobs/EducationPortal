from django.db import models

QUESTION_TYPES = [('Single Answer','Single Answer'),('Multi Answer','Multi Answer'),('User Input','User Input')]

class QuizCategories(models.Model):
    category_name = models.CharField(max_length=50, unique=True)
    
    class Meta:
        verbose_name_plural = 'Quiz Categories'
        ordering = ['category_name']

    def __str__(self):
        return f'{self.category_name}'

class Quiz(models.Model):
    name = models.CharField(max_length=50, null=False)
    description = models.CharField(max_length=300, null=False)
    category_name = models.ForeignKey(QuizCategories, on_delete=models.SET_DEFAULT, default=None)

    class Meta:
        verbose_name_plural = 'Quiz'
        ordering = ['category_name']

    def __str__(self):
        return f'{self.name} ({self.category_name})'

class QuizQuestion(models.Model):
    question_text = models.TextField(null=False)
    question_code = models.TextField(null=True)
    question_type = models.CharField(max_length= 20, null=True, choices=QUESTION_TYPES, default='Single Answer')
    question_points = models.IntegerField(null=False, default=1)
    linked_quiz = models.ForeignKey(Quiz, on_delete=models.PROTECT, null=False)

    def __str__(self):
        return f'{self.question_text[:30]}...'


class QuizAnswers(models.Model):
    summary = models.TextField(null=False)
    correct_flag = models.BooleanField()
    linked_question = models.ForeignKey(QuizQuestion, on_delete=models.PROTECT, null=False)

    def __str__(self):
        return f'{self.linked_question} ({self.correct_flag})'

class ActiveQuiz(models.Model):
    name = models.CharField(max_length= 50, null=False)
    category_name = models.CharField(max_length= 50, null=False)
    question = models.ForeignKey(QuizQuestion, on_delete=models.SET_DEFAULT, default=None) 
    question_done_flag = models.BooleanField(null=True)
    correct_answer_flag = models.BooleanField(null=True)
    started_at = models.DateTimeField(auto_now_add=True)
    finished_at = models.DateTimeField()
