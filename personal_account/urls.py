from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.acc_page_load, name='acc_page'),
    path('<int:num>/', views.view_load, name='view_page'),
    path('add/', views.createDoc, name='add'),
    path('addpassport/', views.addPassword_page_load, name='addPassp'),
    

]
