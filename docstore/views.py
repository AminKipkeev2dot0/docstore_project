from django.shortcuts import render,redirect
from django.contrib.auth.forms import  UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.db import IntegrityError

def login_page_load(request):
    return render(request, 'docstore/login_page.html')

def registr_page_load(request):
    if request.method=='GET':
        return render(request, 'docstore/registration_page.html',{'form':UserCreationForm()})
    else:
        if request.POST['password1']==request.POST['password2']:
            try:
                user=User.objects.create_user(request.POST['username'],password=request.POST['password1'])
                user.save()
                login(request,user)
                return redirect('login')
            except IntegrityError:
                return render(request, 'docstore/registration_page.html',{'form':UserCreationForm(),'error':'Имя пользователя уже занято, используйте другое'})

        else:
            return render(request, 'docstore/registration_page.html',{'form':UserCreationForm(),'error':'Passwords did not match'})

def login_page_load(request):
    if request.method=='GET':
        return render(request, 'docstore/login_page.html',{'form':AuthenticationForm()})
    else:
        user=authenticate(request,username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'docstore/login_page.html',{'form':AuthenticationForm(),'error':'Неправильное имя пользователя или пароль'})
        else: 
            login(request,user)
            return redirect('acc_page')
def logout_load(request):
    if request.method=='POST':
        logout(request)
        return redirect('login')
    else:return redirect('login')
def forgot_pass_page_load(request):
    return render(request, 'docstore/forgot_password_page.html')