'''
Created on May 20, 2018

@author: jindalr
'''
from django.contrib import admin
from .models import *

#Pet_Type, Pet_Breed, Pet_Owner_Interests, Search

admin.site.register(Pet_Type)
admin.site.register(Pet_Breed)
admin.site.register(Pet_Owner_Interests)
admin.site.register(Search)
admin.site.register(Pet_Parent)
admin.site.register(Pet)
admin.site.register(Pet_Owner_Interest_Ref)
