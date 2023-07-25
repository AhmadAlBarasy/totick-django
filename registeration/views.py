from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout
from .forms import RegisterForm 
# Create your views here.
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save() 
            return redirect('/')
        else:
            return render(request,"registration/register-page.html",{"form":form,"valid":False})
    else:
        if request.user.is_authenticated:
            logout(request)
            return redirect('/register')
        else:
            form = RegisterForm()
            return render(request,"registration/register-page.html",{"form":form,"valid":True})