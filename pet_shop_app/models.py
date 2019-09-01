
from django.db import models
from django.urls import reverse


# Create your models here.
class Pet (models.Model) :
    name = models.CharField(max_length=50)
    age = models.IntegerField() 
    available = models.BooleanField(default=True)
    image = models.ImageField(null=True,blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__ (self):
        return self.name

    def get_absolute_url (self) :
        return reverse ('pet-detail', kwargs={'pet_id':self.id})
