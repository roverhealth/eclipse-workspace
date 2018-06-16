from django.contrib import admin
from django import forms
from . models import *

class PetAdmin(admin.ModelAdmin):
    list_display = ('user', 'pet_name', 'gender', 'pet_type', 'pet_breed', 'age', 'weight', 'special_inst', 'photo')
     
    def get_queryset(self, request):
        queryset = super(PetAdmin, self).get_queryset(request)
        queryset = queryset.order_by('pet_name','user')
        return queryset


# def breedform_factory(pet_type):
#         class breedForm(forms.ModelForm):
#             m_file = forms.ModelChoiceField(
#                 queryset=Pet_Breed.objects.filter(type=pet_type)
#         )
#         return breedForm
# 
# class breedAdmin(admin.ModelAdmin):
# 
#     def get_form(self, request, obj=None, **kwargs):
#         if obj is not None and obj.type is not None:
#             kwargs['form'] = breedform_factory(obj.type)
#         return super(breedAdmin, self).get_form(request, obj, **kwargs)
    
admin.site.register(Pet_Type)
admin.site.register(Pet_Breed)
admin.site.register(Pet_Owner_Interests)
admin.site.register(Pet, PetAdmin)
admin.site.register(Search)



