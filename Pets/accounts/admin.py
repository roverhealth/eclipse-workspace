# Register your models here.
from django.contrib import admin
from . models import *   
     
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'city_name', 'zip_code', 'cell_phone_number', 'own_a_pet')
     
    def city_name(self, obj):
        return obj.city
    
    def get_queryset(self, request):
        queryset = super(UserProfileAdmin, self).get_queryset(request)
        queryset = queryset.order_by('-cell_phone_number','user')
        return queryset

admin.site.register(UserProfile, UserProfileAdmin)

admin.site.site_header = 'Pet Extended Family Administration'