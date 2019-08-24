""" Unit tests for testsystem application """
from django.test import TestCase
from .models import Quiz, QuizCategories, QuizQuestion

# Create your tests here.


class CustomQuiz(TestCase):
    """ Test for Quiz module """

    def test_create_quiz_category(self):
        """ cetegory test """
        quiz_category = QuizCategories.objects.create(
            category_name='Test Category'
        )
        self.assertEqual(quiz_category.category_name, 'Test Category')

    def test_create_quiz(self):
        """ quiz test """
        quiz_category = QuizCategories.objects.create(
            category_name='Test Category'
        )

        quiz = Quiz.objects.create(
            name='Test Quiz',
            description='Short Description',
            category_name=quiz_category
        )

        self.assertEqual(quiz.name, 'Test Quiz')
        self.assertEqual(quiz.description, 'Short Description')

    def test_create_questions(self):
        """ questions test """
        quiz_category = QuizCategories.objects.create(
            category_name='Test Category'
        )

        quiz = Quiz.objects.create(
            name='Test Quiz',
            description='Short Description',
            category_name=quiz_category
        )

        question = QuizQuestion.objects.create(
            question_text='Test question',
            question_code='Test question code',
            question_type='Single Answer',
            question_points=1,
            linked_quiz=quiz,
            answers_dict={'a1': 0, 'a2': 0}
        )

        self.assertIsInstance(question.answers_dict, dict)

    def test_answers_for_dict(self):
        """ get_answers() function test - (for correct format of questions)"""
        answers = [q.answers_dict for q in QuizQuestion.objects.all()]

        for answer in answers:
            self.assertIsInstance(answer.answers_dict, dict)
