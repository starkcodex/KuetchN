from django.shortcuts import render, HttpResponsePermanentRedirect, redirect
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    return render(request, 'core/home.html')
