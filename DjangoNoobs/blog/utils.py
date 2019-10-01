"""
Mixins (using in views) for Blog application
"""


from django.http import JsonResponse
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.core.paginator import Paginator
from django.template.loader import render_to_string


class ObjectListMixin:
    """ Mixin for render list page Post, Tag, Category """
    model = None
    template = None
    paginate_items = None

    def get(self, request):
        """ GET method for ObjectListMixin """
        obj = self.model.objects.all()
        paginator = Paginator(obj, self.paginate_items)

        page_number = request.GET.get('page', 1)  # default = 1
        page = paginator.get_page(page_number)

        is_paginated = page.has_other_pages()

        if page.has_previous():
            prev_url = '?page={}'.format(page.previous_page_number())
        else:
            prev_url = ''

        if page.has_next():
            next_url = '?page={}'.format(page.next_page_number())
        else:
            next_url = ''

        context = {
            'page_object': page,
            'is_paginated': is_paginated,
            'prev_url': prev_url,
            'next_url': next_url,
            'detail': True,
        }
        return render(request, self.template, context=context)


class ObjectDetailMixin:
    """ Mixin for render detail page for Post, Tag, Category """
    model = None
    template = None

    def get(self, request, slug):
        """ GET method for ObjectDetailMixin """
        obj = get_object_or_404(self.model, slug__iexact=slug)
        return render(request, self.template, context={self.model.__name__.lower(): obj,
                                                       'admin_object': obj,
                                                       'detail': True
                                                       })


class ObjectCreateMixin:
    """ Mixin for render create page for Post, Tag, Category """
    form_model = None
    template = None

    def get(self, request):
        """ GET method for ObjectCreateMixin """
        form = self.form_model()
        return render(request, self.template, context={'form': form})

    def post(self, request):
        """ POST method for ObjectCreateMixin """
        bound_form = self.form_model(request.POST)
        if bound_form.is_valid():
            bound_form.instance.author = request.user
            new_obj = bound_form.save()
            return redirect(new_obj)
        return render(request, self.template, context={'form': bound_form})


class ObjectUpdateMixin:
    """ Mixin for render edit page for Post, Tag, Category """
    model = None
    form_model = None
    template = None

    def get(self, request, slug):
        """ GET method for ObjectUpdateMixin """
        obj = self.model.objects.get(slug__iexact=slug)
        bound_form = self.form_model(instance=obj)
        context = {'form': bound_form, self.model.__name__.lower(): obj}
        return render(request, self.template, context=context)

    def post(self, request, slug):
        """ POST method for ObjectUpdateMixin """
        obj = self.model.objects.get(slug__iexact=slug)
        bound_form = self.form_model(request.POST, instance=obj)
        if bound_form.is_valid():
            updated_obj = bound_form.save()
            return redirect(updated_obj)
        context = {'form': bound_form, self.model.__name__.lower(): obj}
        return render(request, self.template, context=context)


class ObjectDeleteMixin:
    """ Mixin for render delete page for Post, Tag, Category """
    model = None
    template = None
    redirect_url = None

    def get(self, request, slug):
        """ GET method for ObjectDeleteMixin """
        obj = self.model.objects.get(slug__iexact=slug)
        return render(request, self.template, context={self.model.__name__.lower(): obj})

    def post(self, slug):
        """ POST method for ObjectDeleteMixin """
        obj = self.model.objects.get(slug__iexact=slug)
        obj.delete()
        return redirect(reverse(self.redirect_url))


class LikeDislikeMixin:
    """ Mixin for likes and dislikes for Comments and Posts (and other models if need it) """
    model = None
    get_model = None
    type = None
    template = None

    def post(self, request):
        """ POST method for LikeDislikeMixin """
        obj = get_object_or_404(self.model, id=request.POST.get(self.get_model))
        if self.type == 'likes':
            # if like is already exist - remove him (reply click like-button)
            if obj.likes.filter(id=request.user.id).exists():
                obj.likes.remove(request.user)
            else:
                # create like
                obj.likes.add(request.user)
                # with creating like, check dislike - if exists, remove him
                if obj.dislikes.filter(id=request.user.id).exists():
                    obj.dislikes.remove(request.user)
        elif self.type == 'dislikes':
            # if dislike is already exist - remove him (reply click dislike-button)
            if obj.dislikes.filter(id=request.user.id).exists():
                obj.dislikes.remove(request.user)
            else:
                # create dislike
                obj.dislikes.add(request.user)
                # with creating dislike, check like - if exists, remove him
                if obj.likes.filter(id=request.user.id).exists():
                    obj.likes.remove(request.user)

        context = {self.model.__name__.lower(): obj}
        if request.is_ajax():
            html = render_to_string(self.template, context, request=request)
            return JsonResponse({'form': html})
        # pylint error R1710: Either all return statements in a function should return
        # an expression, or none of them should. (inconsistent-return-statements)
        return None
