from django.shortcuts import render, HttpResponse


# Create your views here.
def profile_view(request):
    return render(request, 'registration/profile.html')


def sing_up_view(request):
    return render(request, 'registration/sing_up.html')


# Create your views here.
