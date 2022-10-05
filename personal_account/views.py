from django.shortcuts import render

# Create your views here.
def acc_page_load(request):
    return render(request, 'personal_account/acc_page.html')