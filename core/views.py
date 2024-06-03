from . import forms
from django.shortcuts import render, redirect
from django.contrib.auth import login

from django.contrib.auth.decorators import login_required


def hero_page(request):
    return render(request, 'core/hero.html')

@login_required
def home(request):
    return render(request, 'core/home.html')

def sign_up(request):
    form = forms.SignUpForm()
    
    if request.method == 'POST':
        form = forms.SignUpForm(request.POST)
        
        if form.is_valid():
            email = form.cleaned_data['email'].lower()
            user = form.save(commit=False)
            user.username = email
            user.save()
            
            login(request, user)
            return redirect('/')
        
    
    
    return render(request, 'auth/sign_up.html', {
        'form': form
    })

@login_required
def customer(request):
    return render(request, 'core/home.html')

@login_required
def courier(request):
    return render(request, 'core/home.html')