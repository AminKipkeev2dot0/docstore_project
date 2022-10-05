from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.acc_page_load),

]
