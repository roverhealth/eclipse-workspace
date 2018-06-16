from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    post = models.CharField(max_length = 500)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
class Pet_Type (models.Model):
    pet_type = models.CharField(max_length=30)
    add_date = models.DateTimeField('Date Pet Type added', auto_now_add = True)
    
    def __str__(self):
        return self.pet_type

class Pet_Breed (models.Model):
    pet_type = models.ForeignKey(Pet_Type, on_delete=models.CASCADE)
    Pet_Breed = models.CharField(max_length=50)
    country = models.CharField(max_length=50, null=True,blank=True)
    origin  = models.CharField(max_length=50, null=True,blank=True) 
    body_type = models.CharField(max_length=50, null=True,blank=True)   
    Add_Date = models.DateTimeField('Date Pet Breed added', auto_now_add = True)
    
    def __str__(self):
        return self.Pet_Breed

class Pet_Owner_Interests (models.Model):
    Interest_Desc = models.CharField(max_length=60)
    Add_Date = models.DateTimeField('Date Pet Owner Interest added', auto_now_add = True)  
    
    def __str__(self):
        return self.Interest_Desc
    
class Pet_Owner_Interest_Ref (models.Model):
    interest_id = models.ManyToManyField(Pet_Owner_Interests)
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    add_date = models.DateTimeField('Date Pet added', auto_now_add = True)  
    
    def __str__(self):
        return self.interest_id
    
class Pet (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pet_name = models.CharField(max_length=50, null=True,blank=True)
    gender = models.CharField(max_length=1, choices=(('M', 'Male'), ('F', 'Female')), default = 'Male')
    pet_type = models.ForeignKey(Pet_Type, on_delete=models.CASCADE)
    pet_breed =  models.ForeignKey(Pet_Breed, on_delete=models.CASCADE,  null=True,blank=True)
    age = models.CharField(max_length=5, null=True,blank=True)
    weight = models.CharField(max_length=5, null=True,blank=True)
    special_inst = models.CharField(max_length=255, null=True,blank=True)
    photo = models.ImageField(upload_to='profile_images', blank=True)
    add_date = models.DateTimeField('Date Pet added', auto_now_add = True) 
    
    def __str__(self):
        return self.pet_name  
   
class Search (models.Model):
    search_Date = models.DateTimeField('Search Date', auto_now_add = True)
    pet_type = models.ForeignKey(Pet_Type, on_delete=models.CASCADE)
    pet_breed_type = models.ForeignKey(Pet_Breed, on_delete=models.CASCADE)
    zip_code = models.CharField(max_length=15)                    