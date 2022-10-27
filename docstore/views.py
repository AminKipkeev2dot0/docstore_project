from django.shortcuts import render

def login_page_load(request):
    return render(request, 'docstore/login_page.html')

def registr_page_load(request):
    return render(request, 'docstore/registration_page.html')

def forgot_pass_page_load(request):
    return render(request, 'docstore/forgot_password_page.html')

def data_send_email(request):
    return render(request, 'docstore/password_send_email.html')

