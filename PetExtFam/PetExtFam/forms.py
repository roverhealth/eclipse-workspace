from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from PetExtFam.models import Pet_Parent

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required='True')
    
    class Meta:
        model = User
        fields = ('username',
                  'first_name',
                  'last_name',
                  'email',
                  'password1',
                  'password2'
                  )
         
    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
         
        if commit:
            user.save()
 
        return user
    
class EditProfileForm(UserChangeForm):
    
    class Meta:
        model = User
        fields = ('first_name',
                'last_name',
                'email',
                'password'
            )


# class PetParentForm(forms.ModelForm):
#     
#     class Meta:
#         model = Pet_Parent
#         fields = [ 'address','city','state','zip_code','phone_number','fax_number','cell_phone_number','own_a_pet',
#                   'gender',
#                   'image',]
#         help_texts = {
#             'address': ('Address: '),
#             'city': ('City: '),
#             'state': ('State: '),
#             'zip_code': ('Zip Code: '),
#             'phone_number': ('Phone: '),
#             'fax_number': ('Fax: '),
#             'cell_phone_number': ('Cell: '),
#             'own_a_pet' : ('Do you own a pet: '),
#             'gender': ('Gender: '),
#             'image': ('Upload your picture: '),
#         }
