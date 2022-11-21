from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Doc
from .forms import DocForm
from django.urls import reverse_lazy

# Create your views here.
# def acc_page_load(request):
#     docs=Doc.objects.all()
#     return render(request, 'personal_account/acc_page.html',{'docs':docs})

def acc_page_load(request):
        docs=Doc.objects.all()
        return render(request, 'personal_account/acc_page.html',{'docs':docs})

def addPassword_page_load(request):
        return render(request, 'personal_account/add_passp_page.html')

class DocCreateView(CreateView):
    template_name='personal_account/add_page.html'
    form_class=DocForm
    success_url=reverse_lazy('acc_page')
    def get_context_data(self, **kwargs):
          return super().get_context_data(**kwargs)
    