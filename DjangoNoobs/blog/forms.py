from django import forms
from django.core.exceptions import ValidationError
from .models import Tag, Category, Post


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['name', 'slug']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()
        if new_slug == 'create':
            raise ValidationError('Slug may not be "Create"')
        # Пока эта проверка мешает редактированию объекта, так как не дает сохранить слаг без изменения
        # if Tag.objects.filter(slug__iexact=new_slug).count():
        #   raise ValidationError('Slug "{}" is already'.format(new_slug))
        return new_slug


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'slug', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }

    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()
        if new_slug == 'create':
            raise ValidationError('Slug may not be "Create"')
        # Пока эта проверка мешает редактированию объекта, так как не дает сохранить слаг без изменения
        #if Category.objects.filter(slug__iexact=new_slug).count():
         #   raise ValidationError('Slug "{}" is already'.format(new_slug))
        return new_slug


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        # fields = ['title', 'author', 'slug', 'category', 'tags', 'text', 'image']
        fields = ['title', 'slug', 'category', 'tags', 'text', 'image']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            # 'author': forms.Select(attrs={'class': 'form-control'}),  # авто устанавливается из user
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'tags': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'text': forms.Textarea(attrs={'class': 'form-control'}),
            # 'image': forms.ImageField(attrs={'class': 'form-control'}),
        }

    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()
        if new_slug == 'create':
            raise ValidationError('Slug may not be "Create"')
        # Пока эта проверка мешает редактированию объекта, так как не дает сохранить слаг без изменения
        # if Post.objects.filter(slug__iexact=new_slug).count():
        #    raise ValidationError('Slug "{}" is already'.format(new_slug))
        return new_slug
