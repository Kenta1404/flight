from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.



class User(AbstractUser):
    
    phone_number = models.CharField( ("phone_number"),null=False, blank=False, unique=False, max_length=11)
    ID_code = models.CharField ( ("ID_code"),null=False, blank=False, unique=False, max_length=13)
    
    def __str__(self):
         return f"{self.id}: {self.first_name} {self.last_name}"
    

class Place(models.Model):
     code = models.CharField(max_length=3, null= False, blank = False)
     city = models.CharField(max_length=64, null= False, blank = False)
     country = models.CharField(max_length = 64, null= False, blank = False)
     airport = models.CharField(max_length= 64, null= False, blank = False)

     def __str__(self):
        return f"{self.code}: {self.city}, ({self.country})"
     
class Week(models.Model):
    number = models.IntegerField()
    name = models.CharField(max_length=32)

    def __str__(self):
        return f"{self.name} ({self.number})"
    
class Flight(models.Model):
    depart= models.ForeignKey(Place, on_delete=models.CASCADE, related_name="departures")
    destination = models.ForeignKey(Place, on_delete=models.CASCADE, related_name="arrivals")
    depart_time = models.TimeField(auto_now=False, auto_now_add=False)
    depart_day= models.ManyToManyField(Week, related_name="flight_of_the_days")
    duration = models.DurationField(null=False, blank=False)
    arrival_time = models.TimeField(auto_now=False, auto_now_add=False)
    plane = models.CharField(max_length=32)
    airline= models.CharField(max_length=32)
    economy_fare = models.FloatField(null=True)
    business_fare = models.FloatField(null=True)
    first_fare = models.FloatField(null=True)

    def __str__(self):
        return f"{self.id} {self.plane}: {self.depart} to {self.destination}"