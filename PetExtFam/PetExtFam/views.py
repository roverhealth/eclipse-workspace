'''
Created on May 20, 2018

@author: jindalr
'''
from django.shortcuts import render, redirect
#from django.views.generic import TemplateView

from django.contrib.auth.forms import ( UserChangeForm, 
                                        PasswordChangeForm)


from PetExtFam.forms import (
    RegistrationForm, 
    EditProfileForm,
#     PetParentForm
    )

from django.contrib.auth import update_session_auth_hash
from django.urls import reverse

def home(request):
    return render(request, 'PetExtFam/home.html') 

#def AboutView(TemplateView):
#    template_name ='about.html'

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
        return render(request,'PetExtFam/reg_form.html', args)

def view_profile(request):
        args = {'user':request.user}
        return render(request, 'PetExtFam/profile.html', args)   

    
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
            return render(request, 'PetExtFam/edit_profile.html', args)       

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
            return render(request, 'PetExtFam/change_password.html', args)        

# def petparent(request):        
#     
#     Pet_Parent_Form = PetParentForm(request.POST)
#     
#     if Pet_Parent_Form.is_valid():
#            context = RequestContext(request)
#     if request.method == 'POST':
#         petparent_form = PetParentForm(data=request.POST)
#        
#         if petparent_form.is_valid():
#             petparent = petparent_form.save(commit=False)
#             petparent.user = request.user
#             petparent.save()
#         else:
#             print petparent_form.error
#     else:
#         petparent_form = PetParentForm()
#             
#     return render_to_response(
#                 'PriceMyVet/petparent.html',
#                 {'petparent_form': petparent_form },
#                 context)           