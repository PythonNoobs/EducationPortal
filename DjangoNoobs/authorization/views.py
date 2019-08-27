from django.shortcuts import render, HttpResponse
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required #не позволяет просматривать вьюху без авторизации. (здорово)
def profile_view(request):
    return render(request, 'registration/profile.html')


class SignUpFormView(FormView):
    """Создание и небольшая настройка вьюхи регистрации

    Здесь мы устанавливаем куда перейдёт пользователь в случае успешной регистрации, 
    где взять шаблон и реализуем функцию form_valid, 
    которая по умолчанию просто редиректит юзера по ссылке success_url."""

    form_class = UserCreationForm
    success_url = "/accounts/login/"
    template_name = "registration/sign_up.html/"

    def form_valid(self, form):
        form.save()
        return super(SignUpFormView, self).form_valid(form)


#https://ustimov.org/posts/17/
#https://developer.mozilla.org/ru/docs/Learn/Server-side/Django/%D0%90%D1%83%D1%82%D0%B5%D0%BD%D1%82%D0%B8%D1%84%D0%B8%D0%BA%D0%B0%D1%86%D0%B8%D1%8F
