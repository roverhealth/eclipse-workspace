'''
Created on May 20, 2018

@author: jindalr
'''
from django.contrib import admin
from .models import *

#Pet_Type, Pet_Breed, Pet_Owner_Interests, Search
class Pet_BreedAdmin(admin.ModelAdmin):
    list_display = ('Pet_Breed', 'pet_type')
    
class Pet_Admin(admin.ModelAdmin):
    list_display = ('pet_name', 'user', 'pet_type', 'pet_breed')    
    
class Pet_Owner_Interest_Ref_Admin(admin.ModelAdmin):
    list_display = ('interest_id', 'user')    
    
    
class Pet_ParentAdmin(admin.ModelAdmin):
    list_display = ('user', 'city', 'zip_code', 'cell_phone_number', 'own_a_pet', 'email')
    
    def get_queryset(self, request):
        queryset = super(Pet_ParentAdmin, self).get_queryset(request)
        queryset = queryset.order_by('-cell_phone_number','user')
        return queryset
    
admin.site.register(Pet_Type)
admin.site.register(Pet_Breed, Pet_BreedAdmin)
admin.site.register(Pet_Owner_Interests)
admin.site.register(Search)
admin.site.register(Pet_Parent, Pet_ParentAdmin)
admin.site.register(Pet, Pet_Admin)
admin.site.register(Pet_Owner_Interest_Ref, Pet_Owner_Interest_Ref_Admin)

admin.site.site_header = 'Pet Extended Family Administration'


