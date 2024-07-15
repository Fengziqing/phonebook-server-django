from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.
class People(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(validators = [MinLengthValidator(2)],max_length=30,blank='false')
    number = models.CharField(validators = [MinLengthValidator(1)],max_length=13,blank='false')
    