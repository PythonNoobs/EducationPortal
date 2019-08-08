from django.shortcuts import render, HttpResponse
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def profile_view(request):
    return render(request, 'registration/profile.html')


def sign_up_view(request):
    return render(request, 'registration/sign_up.html')

class SignUpFormView(FormView):
    form_class = UserCreationForm

    

    success_url = "/accounts/login/"

    template_name = "registration/sign_up.html/"

    def form_valid(self, form):
        form.save()

        return super(SignUpFormView, self).form_valid(form)

#https://ustimov.org/posts/17/


# Create your views here.
