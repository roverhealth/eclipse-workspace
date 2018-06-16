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

class UserProfile (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=30, null=True,blank=True)
    city = models.CharField(max_length=30, null=True,blank=True)
    state = models.CharField(max_length=2, choices=STATE_CHOICES, default = 'Illinois')
    zip_code = models.CharField(max_length=15, null=True,blank=True)
    phone_number = models.CharField(max_length=20, null=True,blank=True)
    fax_number = models.CharField(max_length=20, null=True,blank=True)
    cell_phone_number = models.CharField(max_length=20, null=True,blank=True)
    own_a_pet = models.CharField(max_length=1, choices=(('Y', 'Yes'), ('N', 'No')), default = 'Yes', null=True,blank=True)
    gender = models.CharField(max_length=1, choices=(('M', 'Male'), ('F', 'Female')), default = 'Male', null=True,blank=True)
    image = models.ImageField(upload_to='profile_image',blank=True)
    add_date = models.DateTimeField('Date Pet Parent added', auto_now_add = True)  
    update_date = models.DateTimeField('Date Pet Parent updated', auto_now_add = True)   
#     
#     #naperville = Pet_ParentManager()
#     
    def __str__(self):
        return self.user.username

def create_UserProfile(sender, **kwargs):
    if kwargs['created']:
        pet_parent = UserProfile.objects.create(user=kwargs['instance'])
     
post_save.connect(create_UserProfile, sender=User)
     
