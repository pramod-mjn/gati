from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Userextend(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
<<<<<<< HEAD
    dob = models.DateField('Date of birth')
    verified = models.BooleanField(default = False)
    vercode = models.CharField(max_length = 30)

=======
    eng_speed = models.IntegerField(default = 0)
    nep_speed = models.IntegerField(default = 0)
    verified = models.IntegerField(default = 0)
    vercode = models.CharField(max_length = 30)

    def __str__(self):
        return self.user.first_name

>>>>>>> 37c339a605e48c23a3f69e3a9b297d9507e67a2b
class Englishtext(models.Model):
   typing_text = models.CharField(max_length = 2000)

   def __str__(self):
       return self.typing_text
    

