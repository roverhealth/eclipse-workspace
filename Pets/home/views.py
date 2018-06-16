from django.views.generic import TemplateView
from django.shortcuts import render
from home.forms import HomeForm, PetForm
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from .models import Pet_Type, Pet_Breed, Pet

class HomeView(TemplateView):
    template_name = 'home/home.html' 
    
    def get(self, request):
        form = HomeForm()
        return render(request, self.template_name, {'form':form})
    
    def post(self, request):
        form = HomeForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
#             print('form is valid')
#             print(form.cleaned_data)
#             text = form.cleand_data("post")
#             print(text)
            
        return render(request, self.template_name, {'form':form}  )

class PetListView(ListView):
    model = Pet
    context_object_name = 'my_pets'


class PetCreateView(CreateView):
    model = Pet
    form_class = PetForm 
    success_url = reverse_lazy('pet_changelist')


class PetUpdateView(UpdateView):
    model = Pet
    form_class = PetForm
    #success_url = 'home/pet_list.html'
    success_url = reverse_lazy('pet_changelist')


def load_breeds(request):
    pet_type_id = request.GET.get('pet_type')
    breeds = Pet_Breed.objects.filter(pet_type_id=pet_type_id).order_by('pet_breed')
    return render(request, 'home/pet_breed_dropdown.html', {'breeds': breeds})
    
    
# class edit_pet(TemplateView):
#     template_name = 'home/add_or_remove_pet.html' 
#     
#     def get(self, request):
#         pet_form = PetForm()
#         return render(request, self.template_name, {'pet_form':pet_form})
#     
#     def post(self, request):
#         pet_form = PetForm(request.POST)
#         if pet_form.is_valid():
#             post = pet_form.save(commit=False)
#             post.user = request.user
#             post.save()
#         return render(request, self.template_name, {'pet_form':pet_form} ) 