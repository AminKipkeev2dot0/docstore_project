from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic.edit import CreateView
from .models import Doc
from .forms import DocForm
from django.urls import reverse_lazy

def acc_page_load(request):
        docs=Doc.objects.filter(user=request.user)
        return render(request, 'personal_account/acc_page.html',{'docs':docs})

def view_load(request,num):
        now_doc=get_object_or_404(Doc,pk=num)
        docs=Doc.objects.filter(user=request.user)
        return render(request, 'personal_account/view_page.html',{'docs':docs,'doc':now_doc})
def addPassword_page_load(request):
        return render(request, 'personal_account/add_passp_page.html')

def createDoc(request):
        if request.method=='GET':
                return render(request, 'personal_account/add_page.html',{'form':DocForm()})
        else:
                form=DocForm(request.POST,request.FILES)
                newdoc=form.save(commit=False)
                newdoc.user=request.user
                newdoc.save()
                return redirect('acc_page')