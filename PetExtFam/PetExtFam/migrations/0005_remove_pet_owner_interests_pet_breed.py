# Generated by Django 2.0.5 on 2018-06-01 20:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PetExtFam', '0004_pet_parent_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pet_owner_interests',
            name='Pet_Breed',
        ),
    ]
