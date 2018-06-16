from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from forms import *
from datetime import datetime
from django.forms.models import modelformset_factory
from django.conf import settings
import json
def index(request):
    context = RequestContext(request)
    context_dict = {'index_boldmessage': "I am bold form the context in index page"}
    return render_to_response('PriceMyVet/index.html', context_dict, context)

def about(request):
    context = RequestContext(request)
    context_dict = {'abt_boldmessage': "I am bold form the context in about page"}
    return render_to_response('PriceMyVet/about.html', context_dict, context)
    #return HttpResponse("Rango says here is the about page! <a href='/rango/'> Index</a>")

def register(request):        
    context = RequestContext(request)
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        
        if user_form.is_valid():
            user = user_form.save()
            
            user.set_password(user.password)
            user.save()
            
            registered = True
        else:
            print user_form.error
    else:
        user_form = UserForm()

            
    return render_to_response(
                'PriceMyVet/register.html',
                {'user_form': user_form, 'registered': registered},
                context)   
            
def user_login(request):
    context = RequestContext(request)  
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                if request.POST.get('remember_me', None):
                    request.session.set_expiry(settings.KEEP_LOGGED_DURATION)
                login(request, user)
                return HttpResponseRedirect('/PriceMyVet/')
            else:
                return HttpResponse("your PriceMyVet account is disabled")
        else:
            print "Invalid login details: {0}, {1} ".format(username, password)
            return HttpResponse("Invalid login details supplied.")
    else:
        return render_to_response('PriceMyVet/login.html',{}, context)
                
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/PriceMyVet/')

def forgotpassword(request): 
    context = RequestContext(request)
    return render_to_response('PriceMyVet/forgotpassword.html',{}, context)

def search(request):        
    context = RequestContext(request)
    if request.method == 'POST':
        search_form = SearchForm(data=request.POST)
        
        if search_form.is_valid():
            search = search_form.save()
            search.save()           
        else:
            print search_form.error
    else:
        search_form = SearchForm()  
                 
    return render_to_response(
                'PriceMyVet/search.html',
                {'search_form': search_form},
                context)   

def find_services(request, qs=None):
    if qs is None:
        qs = Service_Type.objects.values_list('service_type', flat=True).all()
    if request.GET.get('pet_type'):
        pet_type=request.GET.get('pet_type')
    # create an empty list to hold the results
    results = []
    qs = Service_Type.objects.values_list('service_type', flat=True).filter(name=pet_type).order_by('service_type')
    # iterate over each service_type and append to results list 
    for service_type in qs:
        results.append(service_type)
    # if no results found then append a relevant message to results list
    if not results:
        # if no results then dispay empty message
        results.append(_("No service found")) 
    # return JSON object
    return HttpResponse(simplejson.dumps(results))

def petparent(request):        
    
    context = RequestContext(request)
    if request.method == 'POST':
        petparent_form = PetParentForm(data=request.POST)
       
        if petparent_form.is_valid():
            petparent = petparent_form.save(commit=False)
            petparent.user = request.user
            petparent.save()
        else:
            print petparent_form.error
    else:
        petparent_form = PetParentForm()
            
    return render_to_response(
                'PriceMyVet/petparent.html',
                {'petparent_form': petparent_form },
                context)
    
def vetpractice(request):        
    
    context = RequestContext(request)
    if request.method == 'POST':
        vetpractice_form = VetPracticeForm(data=request.POST)
       
        if vetpractice_form.is_valid():
            vetpractice = vetpractice_form.save(commit=False)
            vetpractice.user = request.user
            vetpractice.save()
        else:
            print vetpractice_form.error
    else:
        vetpractice_form = VetPracticeForm()
            
    return render_to_response(
                'PriceMyVet/vetpractice.html',
                {'vetpractice_form': vetpractice_form },
                context)
    
            
# def manage_pet(request):
#     formset = AuthorFormSet(queryset=Pet.objects.filter(Pet.user=request.user))

# def manage_pet(request):
#     context = RequestContext(request)
#     PetFormSet = modelformset_factory(Pet, max_num=5,  fields=('pet_name', 'gender', 'pet_type', 'pet_breed', 'age', 'weight', 'profile', 'photo',))
#     if request.method == 'POST':
#         formset = PetFormSet(request.POST, request.FILES)
#         if formset.is_valid():
#             formset.save()
#             return HttpResponseRedirect('/PriceMyVet/')
#     else:
#         formset = PetFormSet()
#     return render_to_response("PriceMyVet/manage_pets.html", {
#                 "formset": formset}, 
#                 context)

from django.shortcuts import get_object_or_404, render

def manage_pet(request):
    img_formset = PetFormset(instance=User())
    
    if request.method == 'POST':
            img_formset = PetFormset(request.POST, 
                request.FILES, instance=User)
            if img_formset.is_valid():
                img_formset.save()
                return HttpResponseRedirect('/PriceMyVet/')
    
    return render(request, "PriceMyVet/manage_pets.html", {
        'img_formset': img_formset,
        'action': "Create" 
    })
    

def manage_vet(request):
    img_formset = VetFormset(instance=Practice())
    
    if request.method == 'POST':
            img_formset = VetFormset(request.POST, 
                request.FILES, instance=Practice)
            if img_formset.is_valid():
                img_formset.save()
                return HttpResponseRedirect('/PriceMyVet/')
    
    return render(request, "PriceMyVet/manage_vets.html", {
        'img_formset': img_formset,
        'action': "Create" 
    })
    
        
# def update_pet(request, pet_id):
#     pet = get_object_or_404(Pet, pk=pet_id)
#     
#     form = PetForm(instance=pet)
#     img_formset = PetImageFormset(instance=pet)
# 
#     if request.method == 'POST':
#         form = PetForm(request.POST, instance=pet)
#         if form.is_valid():
#             pet = form.save(commit=False)
#             img_formset = PetImageFormset(request.POST, 
#                             request.FILES, instance=pet)
#             if img_formset.is_valid():
#                 pet.save()
#                 img_formset.save()
#                 return HttpResponseRedirect(reverse('pets:home'))
#     
#     return render(request, "form.html", {
#         'form': form, 
#         'img_formset': img_formset,
#         'action': "Update" 
#     })
#             