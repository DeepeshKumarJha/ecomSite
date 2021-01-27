from django.shortcuts import render, redirect
from .forms import SignupForm
from django.contrib.auth.forms import AuthenticationForm
from django.db import IntegrityError
from django.contrib.auth.models import User
from django.contrib.auth import login , logout , authenticate

def homePageView(request):
    return render(request, 'Login_Signup_App/home.html')

def Signup(request):
    if request.method == 'GET':
        return render(request, 'Login_Signup_App/signup.html', {'form': SignupForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try :
                user = User.objects.create_user(username = request.POST['username'], email = request.POST['email'], password = request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('home')
            except IntegrityError:
                return render(request, 'Login_Signup_App/signup.html', {'form': SignupForm(), 'error':'user name already exists'})
        else:
            return render(request, 'Login_Signup_App/signup.html', {'form': SignupForm(), 'error':'check password'})
        

def loginUser(request):
    if request.method == 'GET':
        return render(request, 'Login_Signup_App/login.html', {'form': AuthenticationForm(), })
    else:
        user = authenticate(request, username = request.POST['username'], password = request.POST['password'])
        if user :
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'Login_Signup_App/login.html', {'form': AuthenticationForm(), 'error':'username password does not match' })


def logoutUser(request):
    
    logout(request)
    return redirect('home')