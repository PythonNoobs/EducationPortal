from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse
from django.utils import timezone
from django.utils.text import slugify


def gen_slug(s):
    new_slug = slugify(s, allow_unicode=True)  # need translit... Пока русские буквы остаются в slug
    return new_slug


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    # slug = models.CharField(max_length=256, blank=True, unique=True)
    slug = models.SlugField(max_length=50, blank=True, unique=True)

    def get_absolute_url(self):
        return reverse('tag_detail_url', kwargs={'slug': self.slug})

    def get_update_url(self):
        return reverse('tag_update_url', kwargs={'slug': self.slug})

    def get_delete_url(self):
        return reverse('tag_delete_url', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = gen_slug(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    # slug = models.CharField(max_length=200, blank=True, unique=True)
    slug = models.SlugField(max_length=150, blank=True, unique=True)
    description = models.TextField()

    def get_absolute_url(self):
        return reverse('category_detail_url', kwargs={'slug': self.slug})

    def get_update_url(self):
        return reverse('category_update_url', kwargs={'slug': self.slug})

    def get_delete_url(self):
        return reverse('category_delete_url', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = gen_slug(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='posts')
    # tags = models.ManyToManyField(Tag)
    tags = models.ManyToManyField(Tag, blank=True, related_name='posts')

    title = models.CharField(max_length=150)
    # slug = models.CharField(max_length=256, blank=True, unique=True)
    slug = models.SlugField(max_length=200, blank=True, unique=True)
    text = models.TextField()
    image = models.ImageField(blank=True, null=True)

    create_date = models.DateTimeField(auto_now=True)
    change_date = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('post_detail_url', kwargs={'slug': self.slug})

    def get_update_url(self):
        return reverse('post_update_url', kwargs={'slug': self.slug})

    def get_delete_url(self):
        return reverse('post_delete_url', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = gen_slug(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        # return str(self.change_date) + ' ' + str(self.title)
        return str(self.title)

    # def save(self):
    #    self.change_date = timezone.localtime(timezone.now()).date()
    #    self.slug = self.title

    class Meta:
        ordering = ['-create_date']
        get_latest_by = 'create_date'


class Mark(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    score = models.FloatField()


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now=True)
    change_date = models.DateTimeField(default=create_date)
