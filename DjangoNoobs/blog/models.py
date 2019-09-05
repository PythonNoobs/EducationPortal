from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Tag(models.Model):
    name = models.CharField(max_length=128, unique=True)
    slug = models.CharField(max_length=256, blank=True, unique=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    slug = models.CharField(max_length=256, blank=True, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.name


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    tags = models.ManyToManyField(Tag)

    title = models.CharField(max_length=128)
    slug = models.CharField(max_length=256, blank=True, unique=True)
    text = models.TextField()
    image = models.ImageField(blank=True, null=True)

    create_date = models.DateTimeField(auto_now=True)
    change_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-create_date']
        get_latest_by = 'create_date'

    def __str__(self):
        return str(self.change_date) + ' ' + str(self.title)

    def save(self):
        self.change_date = timezone.localtime(timezone.now()).date()
        self.slug = self.title


class Mark(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    score = models.FloatField()


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now=True)
    change_date = models.DateTimeField(default=create_date)