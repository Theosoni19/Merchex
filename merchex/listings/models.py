from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Band(models.Model):
    class Genre(models.TextChoices):
        HIP_HOP= 'HH'
        R_N_B = 'RB'
        SYNTH_POP = 'SP'
        ALTERNATIVE_ROCK = 'AR'

    name= models.fields.CharField(max_length=100)
    genre= models.fields.CharField(choices=Genre.choices, max_length=5, default="HH")
    biography= models.fields.CharField(max_length=1000, default="")
    year_formed= models.fields.IntegerField(validators=[MinValueValidator(1900), MaxValueValidator(2022)], default=2000)
    active= models.fields.BooleanField(default=True)
    official_homepage= models.fields.URLField(null=True, blank=True)

    def __str__(self):
        return f'{self.name}'



class Listing(models.Model):
    class Type(models.TextChoices):
        RECORDS = 'RE'
        CLOTHING = 'CL'
        POSTERS = 'PO'
        MISCELLANEOUS = 'MI'
    title= models.fields.CharField(max_length=100)
    description= models.fields.CharField(max_length=1000, default='')
    sold= models.fields.BooleanField(default=False)
    year= models.fields.IntegerField(validators=[MaxValueValidator(2022), MinValueValidator(1900)], null=True)
    type= models.fields.CharField(choices=Type.choices, max_length=5, default='RE')
    band= models.ForeignKey(Band, null=True, on_delete=models.SET_NULL)
    
    def __str__(self):
        return f'{self.title}'
