"""
Classes (Models) for Blog application
"""


from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse
from uuslug import slugify


class Tag(models.Model):
    """ Class for define posts Tag """
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, blank=True, unique=True)

    def get_absolute_url(self):
        """ Method for get absolute url to current tag """
        return reverse('tag_detail_url', kwargs={'slug': self.slug})

    def get_update_url(self):
        """ Method for get update page url to current tag """
        return reverse('tag_update_url', kwargs={'slug': self.slug})

    def get_delete_url(self):
        """ Method for get delete page url to current tag """
        return reverse('tag_delete_url', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        """ Override save method for using slugify """
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Category(models.Model):
    """ Class for define posts Categories """
    name = models.CharField(max_length=128, unique=True)
    slug = models.SlugField(max_length=150, blank=True, unique=True)
    description = models.TextField()

    def get_absolute_url(self):
        """ Method for get absolute url to current category """
        return reverse('category_detail_url', kwargs={'slug': self.slug})

    def get_update_url(self):
        """ Method for get update page url to current category """
        return reverse('category_update_url', kwargs={'slug': self.slug})

    def get_delete_url(self):
        """ Method for get delete page url to current category """
        return reverse('category_delete_url', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        """ Override save method for using slugify """
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Post(models.Model):
    """
    Class for define Post
    Linked to models: User, Category, Tag
    """
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='posts')
    tags = models.ManyToManyField(Tag, blank=True, related_name='posts')

    title = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(max_length=200, blank=True, unique=True)
    text = models.TextField(blank=True)
    likes = models.ManyToManyField(User, related_name='likes', blank=True)
    dislikes = models.ManyToManyField(User, related_name='dislikes', blank=True)

    image = models.ImageField(blank=True, null=True)

    create_date = models.DateTimeField(auto_now_add=True)
    change_date = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        """ Method for get absolute url to current post """
        return reverse('post_detail_url', kwargs={'slug': self.slug})

    def get_update_url(self):
        """ Method for get update page url to current post """
        return reverse('post_update_url', kwargs={'slug': self.slug})

    def get_delete_url(self):
        """ Method for get delete page url to current post """
        return reverse('post_delete_url', kwargs={'slug': self.slug})

    def get_comment_url(self):
        """ Method for get comment url for current post """
        return reverse('post_comment_url', kwargs={'slug': self.slug})

    def total_likes(self):
        """ Method for count total likes for current post """
        return self.likes.count()

    def total_dislikes(self):
        """ Method for count total dislikes for current post """
        return self.dislikes.count()

    def save(self, *args, **kwargs):
        """ Override save method for using slugify """
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-create_date']
        get_latest_by = 'create_date'


class Mark(models.Model):
    """
    Class for define posts Mark
    Linked to models: User, Post
    """
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    score = models.FloatField()


class Comment(models.Model):
    """
    Class for define Comment
    Linked to models: User, Post
    """
    class Meta:
        db_table = "comments"

    path = ArrayField(models.IntegerField())
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    author_id = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)

    likes = models.ManyToManyField(User, related_name='comment_likes', blank=True)
    dislikes = models.ManyToManyField(User, related_name='comment_dislikes', blank=True)

    def __str__(self):
        return self.content[0:200]

    def get_offset(self):
        """ Method for set the level of comment """
        level = len(self.path) - 1
        if level > 5:
            level = 5
        return level

    def get_col(self):
        """ Method for set the number of columns in the grid that the comment will take """
        level = len(self.path) - 1
        if level > 5:
            level = 5
        return 12 - level

    def total_likes(self):
        """ Method for count total likes for current comment """
        return self.likes.count()

    def total_dislikes(self):
        """ Method for count total dislikes for current comment """
        return self.dislikes.count()
