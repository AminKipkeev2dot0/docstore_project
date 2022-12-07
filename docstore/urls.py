"""docstore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from docstore import settings
from django.conf.urls.static import static
import personal_account.urls
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login_page_load,name='login'),
    path('registration/', views.registr_page_load, name='registr'),
    path('logout/', views.logout_load, name='logout'),
    path('forgot_password/', views.forgot_pass_page_load, name='forgot_pass'),
    path('account/', include(personal_account.urls)),

]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
