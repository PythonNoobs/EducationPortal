from django.contrib import admin
from .models import Quiz, QuizCategories, QuizAnswers, QuizQuestion

admin.site.register(Quiz)
admin.site.register(QuizCategories)
admin.site.register(QuizAnswers)
admin.site.register(QuizQuestion)
