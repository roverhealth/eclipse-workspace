'''
Created on May 20, 2018

@author: jindalr
'''
from django.shortcuts import render, redirect
#from django.http import HttpResponse, HttpResponseRedirect
#from django.template import RequestContext
#from django.shortcuts import render_to_response
#from django.contrib.auth import authenticate, login, logout
#from django.contrib.auth.models import User
from django.contrib.auth.forms import ( UserChangeForm, 
                                        PasswordChangeForm)


from accounts.forms import (
    RegistrationForm, 
    EditProfileForm
    )
from django.contrib.auth import update_session_auth_hash
from django.urls import reverse

def home(request):
    return render(request, 'accounts/home.html') 

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
            #return redirect(reverse('home').lstrip('/'))
        else:
             return redirect('/register') 
    else:
        form = RegistrationForm()
        args = {'form':form}
        return render(request,'accounts/reg_form.html', args)

def view_profile(request):
        args = {'user':request.user}
        return render(request, 'accounts/profile.html', args)   

    
def edit_profile(request):
        if request.method == 'POST':
            form = EditProfileForm(request.POST, instance=request.user)
            if form.is_valid():
                form.save()
                return redirect(reverse('view_profile').lstrip('/'))
            else:
                return redirect(reverse('edit_profile').lstrip('/')) 
        else: 
            form = EditProfileForm(instance=request.user)  
            args = {'form': form}
            return render(request, 'accounts/edit_profile.html', args)       

def change_password(request):
        if request.method == 'POST':
            form = PasswordChangeForm(data=request.POST, user=request.user)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user)
                return redirect(reverse('view_profile').lstrip('/'))  
            else:
                return redirect(reverse('change_password').lstrip('/'))
        else: 
            form = PasswordChangeForm(user=request.user)  
            args = {'form': form}
            return render(request, 'accounts/change_password.html', args)           