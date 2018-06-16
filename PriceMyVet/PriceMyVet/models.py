from django.db import models
from django.contrib.auth.models import User

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
    add_date = models.DateField('Date Pet Type added', auto_now_add = True)
 
    def __unicode__(self):
        return self.pet_type
    
class Pet_Breed (models.Model):
    pet_type = models.ForeignKey(Pet_Type)
    Pet_Breed = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    origin  = models.CharField(max_length=50) 
    body_type = models.CharField(max_length=50)   
    coat  = models.CharField(max_length=50)
    pattern = models.CharField(max_length=50) 
    Add_Date = models.DateField('Date Pet Breed added', auto_now_add = True)
 
    def __unicode__(self):
        return self.Pet_Breed

class Service_Type (models.Model):
    pet_type = models.ForeignKey(Pet_Type)
    service_type = models.CharField(max_length=100)
    Add_Date = models.DateField('Date Service Type added', auto_now_add = True)
 
    def __unicode__(self):
        return self.service_type

class Search (models.Model):
    search_Date = models.DateField('Search Date', auto_now_add = True)
    pet_type = models.ForeignKey(Pet_Type)
    service_type = models.ForeignKey(Service_Type)
    zip_code = models.CharField(max_length=15)
    radius = models.CharField(max_length=5)

class Pet_Parent (models.Model):
    user = models.ForeignKey(User)
    address = models.CharField(max_length=30, null=True,blank=True)
    city = models.CharField(max_length=30, null=True,blank=True)
    state = models.CharField(max_length=2, choices=STATE_CHOICES, default = 'Illinois')
    zip_code = models.CharField(max_length=15, null=True,blank=True)
    phone_number = models.CharField(max_length=20, null=True,blank=True)
    fax_number = models.CharField(max_length=20, null=True,blank=True)
    cell_phone_number = models.CharField(max_length=20, null=True,blank=True)
    gender = models.CharField(max_length=1, choices=(('M', 'Male'), ('F', 'Female')), default = 'Male', null=True,blank=True)
    
class Pet (models.Model):
    user = models.ForeignKey(User)
    pet_name = models.CharField(max_length=50, null=True,blank=True)
    gender = models.CharField(max_length=1, choices=(('M', 'Male'), ('F', 'Female')), default = 'Male')
    pet_type = models.ForeignKey(Pet_Type, default='Dog')
    pet_breed =  models.ForeignKey(Pet_Breed, null=True,blank=True)
    age = models.CharField(max_length=5, null=True,blank=True)
    weight = models.CharField(max_length=5, null=True,blank=True)
    profile = models.CharField(max_length=255, null=True,blank=True)
    photo = models.ImageField(upload_to='profile_images', blank=True)
    add_date = models.DateField('Date Pet added', auto_now_add = True)
    
class Practice (models.Model):
    user = models.ForeignKey(User)
    practice_name = models.CharField(max_length=50, null=True,blank=True)
    contact_first_name = models.CharField(max_length=50, null=True,blank=True)
    contact_middle_name = models.CharField(max_length=50, null=True,blank=True)
    contact_last_name = models.CharField(max_length=50, null=True,blank=True)
    practice_address = models.CharField(max_length=30, null=True,blank=True)
    city = models.CharField(max_length=30, null=True,blank=True)
    state = models.CharField(max_length=2, choices=STATE_CHOICES, default = 'Illinois')
    zip = models.CharField(max_length=15, null=True,blank=True)
    country = models.CharField(max_length=50, null=True,blank=True) 
    tax_id =  models.CharField(max_length=20, null=True,blank=True)
    practice_profile = models.CharField(max_length=255, null=True,blank=True)
    practice_photo = models.ImageField(upload_to='profile_images', blank=True)
    phone_number = models.CharField(max_length=20, null=True,blank=True)
    fax_number = models.CharField(max_length=20, null=True,blank=True)
    cell_number = models.CharField(max_length=20, null=True,blank=True)
    web_site = models.URLField() 
    add_date = models.DateField('Date Pet Practice added', auto_now_add = True)

class Vet (models.Model):
    practice = models.ForeignKey(Practice)
    first_name = models.CharField(max_length=50, null=True,blank=True)
    middle_name = models.CharField(max_length=50, null=True,blank=True)
    last_name = models.CharField(max_length=50, null=True,blank=True)
    gender = models.CharField(max_length=1, choices=(('M', 'Male'), ('F', 'Female')), default = 'Male')
    licens_number = models.CharField(max_length=30, null=True,blank=True)
    exp_no_of_yr = models.CharField(max_length=5, null=True,blank=True)
    vet_profile = models.CharField(max_length=255, null=True,blank=True)
    email_addr = models.EmailField(null=True,blank=True) 
    phone_number = models.CharField(max_length=20, null=True,blank=True)
    photo = models.ImageField(upload_to='profile_images', blank=True)
    add_date = models.DateField('Date Vet added', auto_now_add = True)