from django import forms
from django.contrib.auth.models import User
from models import *
from django.forms.models import inlineformset_factory

class UserForm(forms.ModelForm):
    user_type_choice  =  (
                  ("1","Pet Owner"),
                  ("2","Veterinarian"),
                  ("3","Pet Sitter"),
                  ("4","Pet Walker"),
                 )

    username = forms.CharField(help_text="Username: ")
    email = forms.CharField(help_text="E-mail: ")
    password = forms.CharField(widget=forms.PasswordInput(), help_text="Password: ")
    first_name = forms.CharField(help_text="First Name: ")
    last_name = forms.CharField(help_text="Last Name: ")
    user_type = forms.ChoiceField(user_type_choice, help_text="I am a: ")
    
    class Meta:
        model = User
        fields = [ 'first_name', 'last_name', 'username',  'password', 'email',]
        

PetFormset = inlineformset_factory(User, Pet,   
    fields=('pet_name','gender', 'pet_type', 'pet_breed','age', 'weight', 'profile', 'photo',), can_delete=True)
        
class SearchForm(forms.ModelForm):
    zip_code = forms.CharField(help_text="Zip Code: ")
    radius = forms.CharField(help_text="Radius: ")
    
    #Code for Cascading values for Pet and Services.
    pet_type = forms.ModelChoiceField(
                queryset=Pet_Type.objects.values_list('pet_type'), 
                empty_label='Not Specified', 
                widget=forms.Select(attrs={ 
                                   "onChange":'getService()'})
                )
 
    service_type = forms.ModelChoiceField(
                queryset=Service_Type.objects.values_list('service_type'), 
                empty_label='Not Specified'
                )
    class Meta:
        model = Search
        fields = [ 'pet_type', 'service_type', 'zip_code', 'radius',]
        help_texts = {
             'pet_type': ('Pet Type: '),
             'service_type': ('Service Type: ')
         }


class PetParentForm(forms.ModelForm):
    
    class Meta:
        model = Pet_Parent
        fields = [ 'address','city','state','zip_code','phone_number','fax_number','cell_phone_number','gender',]
        help_texts = {
            'address': ('Address: '),
            'city': ('City: '),
            'state': ('State: '),
            'zip_code': ('Zip Code: '),
            'phone_number': ('Phone: '),
            'fax_number': ('Fax: '),
            'cell_phone_number': ('Cell: '),
            'gender': ('Gender: '),
        }
        
VetFormset = inlineformset_factory(Practice, Vet,   
    fields=('first_name', 'middle_name', 'last_name', 'gender', 'licens_number', 'exp_no_of_yr', 'vet_profile', 'email_addr', 'phone_number','photo',), can_delete=True)

class VetPracticeForm(forms.ModelForm):
    
    class Meta:
        model = Practice
        fields =  ['practice_name', 'practice_address', 
                   'city', 'state', 'zip', 'country', 'tax_id', 'practice_profile', 'practice_photo', 'phone_number','fax_number',
                   'cell_number', 'web_site',]
        help_texts = {'practice_name': ('Practice Name: '),
                     'practice_address': ('Address: '),
                     'city': ('City: '),
                     'state': ('State: '),
                     'zip': ('Zip: '),
                     'country': ('Country: '),
                     'tax_id': ('Tax Id: '),
                     'practice_profile': ('Practice Profile: '),
                     'practice_photo': ('Practice Photo: '),
                     'phone_number': ('Phone Number: '),
                     'fax_number': ('Fax Number: '),
                     'cell_number': ('Cell Number: '),
                     'web_site': ('Web Site address: '),
                     }

# class VetForm(forms.ModelForm):
#     
#     class Meta:
#         model = Vet  
#         fields =  ['first_name', 'middle_name', 'last_name', 'gender', 'licens_number', 'exp_no_of_yr', 'vet_profile', 'email_addr', 'phone_number',]
#         help_texts = {'first_name': ('First Name: '),
#                      'middle_name': ('Middle Name: '),
#                      'last_name': ('Last Name: '),
#                      'gender': ('Gender: '),
#                      'licens_number': ('License Number: '),
#                      'exp_no_of_yr': ('Experience (Years): '),
#                      'vet_profile': ('vet_profile: '),
#                      'email_addr': ('Email: '),
#                      'practice_photo': ('Practice Photo: '),
#                      'phone_number': ('Phone Number: '),
#                      }