from django.shortcuts import render

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

# Create your views here.


def registration(request):
    return render(request, 'accounts/register/registration.html')

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('home:homepage')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/register/register.html', {'form':form})


def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            instance = request.user
            login(request, instance)
        return redirect('home:homepage')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form':form})
