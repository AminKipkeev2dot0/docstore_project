from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic.edit import CreateView
from .models import Doc
from .forms import DocForm
from django.urls import reverse_lazy

def acc_page_load(request):
        docs=Doc.objects.filter(user=request.user)
        return render(request, 'personal_account/acc_page.html',{'docs':docs})

def view_load(request,num):
        now_doc=get_object_or_404(Doc,pk=num,user=request.user)
        docs=Doc.objects.filter(user=request.user)
        return render(request, 'personal_account/view_page.html',{'docs':docs,'doc':now_doc})
def addPassword_page_load(request):
        return render(request, 'personal_account/add_passp_page.html')
def change_load(request,num):
        now_doc=get_object_or_404(Doc,pk=num,user=request.user)
        if request.method=='GET':
                form = DocForm(instance=now_doc)
                return render(request, 'personal_account/change_page.html',{'form':form})
        else: 
                try:
                        form = DocForm(request.POST, instance=now_doc)
                        form.save()
                        return redirect('view_page',num=now_doc.pk)
                except ValueError:
                        return render(request, 'personal_account/change_page.html',{'form':form,'error':'Информация не удовлетворяет требованиям системы'})
def delete_doc(request,num):
        now_doc=get_object_or_404(Doc,pk=num,user=request.user)
        now_doc.delete()
        docs=Doc.objects.filter(user=request.user)
        if docs.count()>0:
                return redirect('view_page',num=docs.first().id)
        else:
                return redirect('acc_page')
def createDoc(request):
        docs=Doc.objects.filter(user=request.user)
        if request.method=='GET':
                return render(request, 'personal_account/add_page.html',{'form':DocForm(),'docs':docs})
        else:
                form=DocForm(request.POST,request.FILES)
                newdoc=form.save(commit=False)
                newdoc.user=request.user
                newdoc.save()
                return redirect('view_page',num=newdoc.id)