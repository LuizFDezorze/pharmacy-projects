from django.shortcuts import render


def home(request):
    return render(request, "home_app/home.html")

def create(request):
    return render(request, "home_app/create.html")

def store(request):
    pass