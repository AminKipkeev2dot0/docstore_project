from django.shortcuts import render,redirect
from django.contrib.auth.forms import  UserCreationForm
from django.contrib.auth.models import User

def login_page_load(request):
    return render(request, 'docstore/login_page.html')

def registr_page_load(request):
    if request.method=='GET':
        return render(request, 'docstore/registration_page.html',{'form':UserCreationForm()})
    else:
        if request.POST['password1']==request.POST['password2']:
            user=User.objects.create_user(request.POST['username'],password=request.POST['password1'])
            user.save()
            return redirect('login')
        else:
            return render(request, 'docstore/registration_page.html',{'form':UserCreationForm(),'error':'Passwords did not match'})

def forgot_pass_page_load(request):
    return render(request, 'docstore/forgot_password_page.html')