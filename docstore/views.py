from django.shortcuts import render

def login_page_load(request):
    return render(request, 'docstore/login_page.html')

def registr_page_load(request):
    return render(request, 'docstore/registration_page.html')

def forgot_pass_page_load(request):
    return render(request, 'docstore/forgot_password_page.html')