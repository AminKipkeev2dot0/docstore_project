from django.shortcuts import render

def login_page_load(request):
    return render(request, 'docstore/login_page.html')