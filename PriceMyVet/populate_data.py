import os

def populate():
    pet_dog = add_pet('Dog')

    add_service(pet=pet_dog, 
            service = "Broken Bones")

    add_service(pet=pet_dog, 
            service = "Cuts and Bruises")

    add_service(pet=pet_dog, 
            service = "Ear Injuries")

    add_service(pet=pet_dog, 
            service = "Electric Shock Injuries")
    
    add_service(pet=pet_dog, 
            service = "Eye Injuries")
    
    add_service(pet=pet_dog, 
            service = "Fishing Accidents")
    
    add_service(pet=pet_dog, 
            service = "Limping")
    
    add_service(pet=pet_dog, 
            service = "Near Drowning")
    
    add_service(pet=pet_dog, 
            service = "Puncture Wounds")
    
    add_service(pet=pet_dog, 
            service = "Swollen Paws")
    
    pet_cat = add_pet('Cat')

    add_service(pet=pet_cat, 
            service = "Vomiting")

    add_service(pet=pet_cat, 
            service = "Feline Lower Urinary Tract Diseases")

    add_service(pet=pet_cat, 
            service = "Fleas")

    add_service(pet=pet_cat, 
            service = "Tapeworms")    

    add_service(pet=pet_cat, 
            service = "Diarrhea")    
    
    for c in Pet_Type.objects.all():
        for p in Service_Type.objects.filter(pet_type=c):
            print "- {0} - {1}".format(str(c), str(p))   

def add_pet(name):
    c = Pet_Type.objects.get_or_create(pet_type=name)[0]
    return c

def add_service(pet, service):
    p= Service_Type.objects.get_or_create(pet_type=pet, service_type=service)[0]
    return p

if __name__ == '__main__':
    print "starting PriceMyVet population script ..."
    os.environ.setdefault('DJANGO_SETTINGS_MODULE','PriceMyVet.settings')
    from PriceMyVet.models import Pet_Type, Service_Type
    populate()
