from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class Person(models.Model):
   firstname = models.CharField(max_length=30)
   lastname = models.CharField(max_length=30)
   dateofbirth = models.DateField()
   zipcode = models.CharField(
      max_length=10,
      validators = [RegexValidator(
         regex = r'^[0-9]{5}(?:-[0-9]{4})?$',
         message = 'Zip code must be in Zip or Zip+4 formats',
         code = 'Invalid zipcode'
      )]
   )

