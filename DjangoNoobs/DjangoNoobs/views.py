from django.contrib import auth
from django.shortcuts import render, redirect


def index(request):
    return render(request, 'index.html')