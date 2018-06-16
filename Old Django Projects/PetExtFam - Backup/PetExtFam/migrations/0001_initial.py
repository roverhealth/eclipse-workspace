# Generated by Django 2.0.5 on 2018-05-21 00:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pet_Breed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Pet_Breed', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
                ('origin', models.CharField(max_length=50)),
                ('body_type', models.CharField(max_length=50)),
                ('Add_Date', models.DateTimeField(auto_now_add=True, verbose_name='Date Pet Breed added')),
            ],
        ),
        migrations.CreateModel(
            name='Pet_Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pet_type', models.CharField(max_length=30)),
                ('add_date', models.DateTimeField(auto_now_add=True, verbose_name='Date Pet Type added')),
            ],
        ),
        migrations.AddField(
            model_name='pet_breed',
            name='pet_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PetExtFam.Pet_Type'),
        ),
    ]
