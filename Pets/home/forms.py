from django import forms
from home.models import Post, Pet, Pet_Breed, Pet_Owner_Interests, Pet_Owner_Interest_Ref
#from home.models import models

class HomeForm(forms.ModelForm):
#     post = forms.CharField()
    
    class Meta:
        model = Post
        fields = ['post',]

class PetForm(forms.ModelForm):    
     
    class Meta:
        model = Pet 
        fields = ['pet_name', 
                'gender', 
                'pet_type', 
                'pet_breed', 
                'age',
                'weight',
                'special_inst',
                'photo',]
    
    # following code is to create a cascaded dropdown between Pty type and Pet Breed.
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['pet_breed'].queryset = Pet_Breed.objects.none()

        if 'pet_type' in self.data:
            try:
                pet_type_id = int(self.data.get('pet_type'))
                self.fields['pet_breed'].queryset = Pet_Breed.objects.filter(pet_type_id=pet_type_id).order_by('pet_type')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['pet_breed'].queryset = self.instance.pet_type.pet_breed.order_by('pet_breed')
#             
# class PetOwnerInterestForm(forms.ModelForm):
#         pet_owner_int = forms.MultipleChoiceField(choices=Pet_Owner_Interests.Interest_Desc, widget=forms.CheckboxSelectMultiple())
#          
#         class Meta:
#             model = Pet_Owner_Interest_Ref
#             fields = (
#                 'interest_id',
#                 )                 