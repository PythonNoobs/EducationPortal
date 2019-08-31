from django.db import models
from django.contrib.auth.models import User


class BlogPost(models.Model):
    # meta
    author = models.ForeignKeyField(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)
    # content
    title = models.CharField(max_length=128)
    text = models.TextField()
    image = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.title + ' ' + str(self.date)
