from django.shortcuts import render
from .models import Doc

# Create your views here.
def acc_page_load(request):
    docs=Doc.objects.all()
    return render(request, 'personal_account/acc_page.html',{'docs':docs})