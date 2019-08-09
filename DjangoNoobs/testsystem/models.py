from django.db import models

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
        ordering = ['name']

    def __str__(self):
        return f'{self.name} ({self.category_name})'

class QuizQuestion(models.Model):
    question_text = models.TextField(null=False)
    question_type = models.CharField(max_length= 50, null=True)
    question_points = models.IntegerField(null=False, default=1)
    linked_quiz = models.ForeignKey(Quiz, on_delete=models.PROTECT, null=False)

class QuizAnswers(models.Model):
    summary = models.TextField(null=False)
    correct_flag = models.BooleanField()
    linked_quiz = models.ForeignKey(QuizQuestion, on_delete=models.PROTECT, null=False)
