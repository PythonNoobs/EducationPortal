"""
Forms classes for Blog application
"""


from django import forms
from django.core.exceptions import ValidationError
from .models import Tag, Category, Post


class TagForm(forms.ModelForm):
    """Class for Tag Form"""
    class Meta:
        model = Tag
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def clean_name(self):
        """
        Method for disable create tag with name 'create'
        and check for already exist names
        """
        new_name = self.cleaned_data['name'].lower()
        if new_name == 'create':
            raise ValidationError('Имя тега не может быть "Create"')
        if Tag.objects.filter(name__iexact=new_name).count():
            raise ValidationError('Тег "{}" уже существует'.format(new_name))
        return new_name


class CategoryForm(forms.ModelForm):
    """ Class for Category Form """
    class Meta:
        model = Category
        fields = ['name', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }

    def clean_name(self):
        """
        Method for disable create category with name 'create'
        and check for already exist names
        """
        new_name = self.cleaned_data['name'].lower()
        if new_name == 'create':
            raise ValidationError('Название категории не может быть "Create"')
        if Category.objects.filter(name__iexact=new_name).count():
            raise ValidationError('Категория "{}" уже существует'.format(new_name))
        return new_name


class PostForm(forms.ModelForm):
    """ Class for Post Form """
    class Meta:
        model = Post
        fields = ['title', 'category', 'tags', 'text', 'image']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'tags': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'text': forms.Textarea(attrs={'class': 'form-control'}),
            # 'image': forms.ImageField(attrs={'class': 'form-control'}),
        }

    def clean_title(self):
        """
        Method for disable create post with name 'create'
        and check for already exist names
        """
        new_title = self.cleaned_data['title'].lower()
        if new_title == 'create':
            raise ValidationError('Название поста не может быть "Create"')
        if Post.objects.filter(title__iexact=new_title).count():
            raise ValidationError('Пост "{}" уже существует'.format(new_title))
        return new_title


class CommentForm(forms.Form):
    """ Class for Comment Form """
    parent_comment = forms.IntegerField(
        widget=forms.HiddenInput,
        required=False
    )

    comment_area = forms.CharField(
        label="Написать комментарий",
        widget=forms.Textarea(attrs={'class': 'form-control'})
    )
