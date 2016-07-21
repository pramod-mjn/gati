from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Userextend(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dob = models.DateField('Date of birth')
    verified = models.BooleanField(default = False)
    vercode = models.CharField(max_length = 30)

class Englishtext(models.Model):
   typing_text = models.CharField(max_length = 2000)

   def __str__(self):
       return self.typing_text
    

