

# Create your views here.

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import LoginForm, RegistrationForm
from .models import User


def user_login(request):
    if request.method == 'POST':

        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = User.userob.filter(username=username, userpassword=password)
            if user:
                return render(request, "vulnerability_scanning/home.html")
            else:
                return render(request, "account/wrong.html")

        else:
            return render(request, "account/wrong.html")
    else:
        form = LoginForm()

    return render(request, "account/login.html", {'form': form})


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            uname = form.cleaned_data['username']
            upassword = form.cleaned_data['password']
            userlist = User.userob.all()
            for user0 in userlist:
                if user0.username == uname:
                    return render(request, "account/register0.html")
            user = User.userob.create(username=uname, userpassword=upassword)
            user.save()
            return render(request, "account/register1.html")
        else:
            return HttpResponse("sorry, you cannot register")
    else:
        form = RegistrationForm()
    return render(request, "account/regist.html", {"form": form})
