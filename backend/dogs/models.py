from __future__ import unicode_literals
from django.db import models


# Create your models here.

class Breed(models.Model):


    name = models.CharField(max_length=200, blank=False, unique=True)
    SIZE_CHOIZES  = (
    ('T', 'Tiny'),
    ('S', 'Small'),
    ('M', 'Medium'),
    ('L', 'Large'),
    )
    size = models.CharField(max_length=1, choices=SIZE_CHOIZES)

    friendliness = models.IntegerField(choices=list(zip(range(1, 6), range(1, 6))))
    trainability = models.IntegerField(choices=list(zip(range(1, 6), range(1, 6))))
    sheddingamount = models.IntegerField(choices=list(zip(range(1, 6), range(1, 6))))
    exerciseneeds = models.IntegerField(choices=list(zip(range(1, 6), range(1, 6))))
    # date_created = models.DateTimeField(auto_now_add=True)
    # date_modified = models.DateTimeField(auto_now=True)
    #sheddingamount = models.IntegerField(choices= [i for i in range(1,5)])

    def __str__(self):
        """A string representation of the model."""
        return self.name

class Dog(models.Model):

    name = models.CharField(max_length=200, blank=False)
    age = models.IntegerField()
    #breed = models.CharField(max_length=50)
    breed = models.ForeignKey(Breed, related_name='DogBreed', on_delete=models.CASCADE)
    gender = models.CharField(max_length=1)
    color = models.CharField(max_length=200)
    favoritefood = models.CharField(max_length=200)
    favoritetoy = models.CharField(max_length=200)

    # date_created = models.DateTimeField(auto_now_add=True)
    # date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """A string representation of the model."""
        return self.name
