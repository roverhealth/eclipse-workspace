'''
Created on May 20, 2018

@author: jindalr
'''
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

STATE_CHOICES = (
        ('AL','Alabama'),
        ('AK','Alaska'),
        ('AZ','Arizona'),
        ('AR','Arkansas'),
        ('CA','California'),
        ('CO','Colorado'),
        ('CT','Connecticut'),
        ('DE','Delaware'),
        ('FL','Florida'),
        ('GA','Georgia'),
        ('HI','Hawaii'),
        ('ID','Idaho'),
        ('IL','Illinois'),
        ('IN','Indiana'),
        ('IA','Iowa'),
        ('KS','Kansas'),
        ('KY','Kentucky'),
        ('LA','Louisiana'),
        ('ME','Maine'),
        ('MD','Maryland'),
        ('MA','Massachusetts'),
        ('MI','Michigan'),
        ('MN','Minnesota'),
        ('MS','Mississippi'),
        ('MO','Missouri'),
        ('MT','Montana'),
        ('NE','Nebraska'),
        ('NV','Nevada'),
        ('NH','New Hampshire'),
        ('NJ','New Jersey'),
        ('NM','New Mexico'),
        ('NY','New York'),
        ('NC','North Carolina'),
        ('ND','North Dakota'),
        ('OH','Ohio'),
        ('OK','Oklahoma'),
        ('OR','Oregon'),
        ('PA','Pennsylvania'),
        ('RI','Rhode Island'),
        ('SC','South Carolina'),
        ('SD','South Dakota'),
        ('TN','Tennessee'),
        ('TX','Texas'),
        ('UT','Utah'),
        ('VT','Vermont'),
        ('VA','Virginia'),
        ('WA','Washington'),
        ('WV','West Virginia'),
        ('WI','Wisconsin'),
        ('WY','Wyoming'),
        )

class Pet_Type (models.Model):
    pet_type = models.CharField(max_length=30)
    add_date = models.DateTimeField('Date Pet Type added', auto_now_add = True)
   
class Pet_Breed (models.Model):
    pet_type = models.ForeignKey(Pet_Type, on_delete=models.CASCADE)
    Pet_Breed = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    origin  = models.CharField(max_length=50) 
    body_type = models.CharField(max_length=50)   
    Add_Date = models.DateTimeField('Date Pet Breed added', auto_now_add = True)

class Pet_Owner_Interests (models.Model):
    Interest_Desc = models.CharField(max_length=60)
    Pet_Breed = models.CharField(max_length=50)
    Add_Date = models.DateTimeField('Date Pet Owner Interest added', auto_now_add = True)  
    
class Pet_Parent (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=30, null=True,blank=True)
    city = models.CharField(max_length=30, null=True,blank=True)
    state = models.CharField(max_length=2, choices=STATE_CHOICES, default = 'Illinois')
    zip_code = models.CharField(max_length=15, null=True,blank=True)
    phone_number = models.CharField(max_length=20, null=True,blank=True)
    fax_number = models.CharField(max_length=20, null=True,blank=True)
    cell_phone_number = models.CharField(max_length=20, null=True,blank=True)
    email = models.CharField(max_length=150, null=True,blank=True)
    own_a_pet = models.CharField(max_length=1, choices=(('Y', 'Yes'), ('N', 'No')), default = 'Yes', null=True,blank=True)
    gender = models.CharField(max_length=1, choices=(('M', 'Male'), ('F', 'Female')), default = 'Male', null=True,blank=True)
    image = models.ImageField(upload_to='profile_image',blank=True)
    add_date = models.DateTimeField('Date Pet Parent added', auto_now_add = True)  
    update_date = models.DateTimeField('Date Pet Parent updated', auto_now_add = True)   
    
    def __str__(self):
        return self.user.username

def create_Pet_Parent_profile(sender, **kwargs):
    if kwargs['created']:
        pet_parent = Pet_Parent.objects.create(user=kwargs['instance'])
    
post_save.connect(create_Pet_Parent_profile, sender=User)
    
class Pet (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pet_name = models.CharField(max_length=50, null=True,blank=True)
    gender = models.CharField(max_length=1, choices=(('M', 'Male'), ('F', 'Female')), default = 'Male')
    pet_type = models.ForeignKey(Pet_Type, on_delete=models.CASCADE, default='Dog')
    pet_breed =  models.ForeignKey(Pet_Breed, on_delete=models.CASCADE,  null=True,blank=True)
    age = models.CharField(max_length=5, null=True,blank=True)
    weight = models.CharField(max_length=5, null=True,blank=True)
    special_inst = models.CharField(max_length=255, null=True,blank=True)
    photo = models.ImageField(upload_to='profile_images', blank=True)
    add_date = models.DateTimeField('Date Pet added', auto_now_add = True) 
    
class Pet_Owner_Interest_Ref (models.Model):
    interest_id = models.ForeignKey(Pet_Owner_Interests, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    add_date = models.DateTimeField('Date Pet added', auto_now_add = True)  

class Search (models.Model):
    search_Date = models.DateTimeField('Search Date', auto_now_add = True)
    pet_type = models.ForeignKey(Pet_Type, on_delete=models.CASCADE)
    pet_breed_type = models.ForeignKey(Pet_Breed, on_delete=models.CASCADE)
    zip_code = models.CharField(max_length=15)
    radius = models.CharField(max_length=5) 