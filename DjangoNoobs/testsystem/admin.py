from django.contrib import admin
from .models import Quiz, QuizCategories, QuizQuestion

admin.site.register(Quiz)
admin.site.register(QuizCategories)
admin.site.register(QuizQuestion)
