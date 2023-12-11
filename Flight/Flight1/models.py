from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    
    phone_number = models.CharField( ("phone_number"),null=False, blank=False, unique=False, max_length=11)
    ID_code = models.CharField ( ("ID_code"),null=False, blank=False, unique=False, max_length=13)
    
    def __str__(self):
         return f"{self.id}: {self.first_name} {self.last_name}"