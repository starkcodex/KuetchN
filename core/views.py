from django.shortcuts import render

def hero_page(request):
    return render(request, 'core/hero.html')


def home(request):
    return render(request, 'core/home.html')


def customer(request):
    return render(request, 'core/home.html')


def courier(request):
    return render(request, 'core/home.html')