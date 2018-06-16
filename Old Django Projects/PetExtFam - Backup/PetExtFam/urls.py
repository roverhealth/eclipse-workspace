"""PetExtFam URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth.views import (
    login, 
    logout, 
    password_reset, 
    password_reset_done,
    password_reset_confirm,
    password_reset_complete
    )


urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^login/$', login, {'template_name':'PetExtFam/login.html'}, name='login'),
    url(r'^logout/$', logout, {'template_name':'PetExtFam/logout.html'}, name='logout'),
    url(r'^register/$', views.register, name='register'),
    url(r'^profile/$', views.view_profile, name='view_profile'),
    url(r'^profile/edit/$', views.edit_profile, name='edit_profile'),
    url(r'^change-password/$', views.change_password, name='change_password'),
    url(r'^reset-password/$', password_reset, {'template_name':'PetExtFam/reset_password.html',
                                               'post_reset_redirect':'password_reset_done', 
                                               'email_template_name':'PetExtFam/reset_password_email.html'}, 
                                               name='reset_password'),
    
    url(r'^reset-password/done$', password_reset_done, {'template_name':'PetExtFam/reset_password_done.html'},  
                                                        name='password_reset_done'),
    
    url(r'^reset-password/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', 
        password_reset_confirm, {'template_name':'PetExtFam/reset_password_confirm.html',
                                 'post_reset_redirect':'password_reset_complete'}, 
                                name='password_reset_confirm'),
    
    url(r'^reset-password/complete$', password_reset_complete, {'template_name':'PetExtFam/reset_password_complete.html'}, 
                                                                name='password_reset_complete'),
    url('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
