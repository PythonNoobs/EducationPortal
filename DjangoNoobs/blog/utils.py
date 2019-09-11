from django.shortcuts import render, redirect, reverse
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator


# Mixin for render list page Post, Tag, Category
class ObjectListMixin:
    model = None
    template = None
    paginate_items = None

    def get(self, request):
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
            'next_url': next_url
        }
        return render(request, self.template, context=context)


# Mixin for render detail page for Post, Tag, Category
class ObjectDetailMixin:
    model = None
    template = None

    def get(self, request, slug):
        obj = get_object_or_404(self.model, slug__iexact=slug)
        return render(request, self.template, context={self.model.__name__.lower(): obj,
                                                       'admin_object': obj,
                                                       'detail': True
                                                       })


# Mixin for render create page for Post, Tag, Category
class ObjectCreateMixin:
    form_model = None
    template = None

    def get(self, request):
        form = self.form_model()
        return render(request, self.template, context={'form': form})

    def post(self, request):
        bound_form = self.form_model(request.POST)
        if bound_form.is_valid():
            bound_form.instance.author = request.user
            new_obj = bound_form.save()
            return redirect(new_obj)
        return render(request, self.template, context={'form': bound_form})


# Mixin for render edit page for Post, Tag, Category
class ObjectUpdateMixin:
    model = None
    form_model = None
    template = None

    def get(self, request, slug):
        obj = self.model.objects.get(slug__iexact=slug)
        bound_form = self.form_model(instance=obj)
        return render(request, self.template, context={'form': bound_form, self.model.__name__.lower(): obj})

    def post(self, request, slug):
        obj = self.model.objects.get(slug__iexact=slug)
        bound_form = self.form_model(request.POST, instance=obj)
        if bound_form.is_valid():
            updated_obj = bound_form.save()
            return redirect(updated_obj)
        return render(request, self.template, context={'form': bound_form, self.model.__name__.lower(): obj})


# Mixin for render delete page for Post, Tag, Category
class ObjectDeleteMixin:
    model = None
    template = None
    redirect_url = None

    def get(self, request, slug):
        obj = self.model.objects.get(slug__iexact=slug)
        return render(request, self.template, context={self.model.__name__.lower(): obj})

    def post(self, request, slug):
        obj = self.model.objects.get(slug__iexact=slug)
        obj.delete()
        return redirect(reverse(self.redirect_url))


