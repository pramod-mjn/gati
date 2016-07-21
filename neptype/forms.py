import string, random
from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import Userextend
from django.core.mail import send_mail
'''class UserForm(ModelForm):
    class Meta:
        model = User, Userextend
        fields = ['first_name', 'last_name', 'dob', 'email', 'username',
        'password']
        widgets = {'password' : forms.PasswordInput(), } '''

class loginform(forms.Form):
    username = forms.CharField(label='Username', max_length=30)
    password = forms.CharField(label='Password', max_length=30, widget =
            forms.PasswordInput)

class UserForm(forms.Form):
    firstname = forms.CharField(label='Name', max_length=30)
    lastname = forms.CharField(label='Last Name', max_length=30)
    dob = forms.DateField(label='Date of Birth')
    email = forms.EmailField(label='Email')
    username = forms.CharField(label='Username', max_length=30)
    password = forms.CharField(label='Password', max_length=30,
            widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', max_length=30,
            widget=forms.PasswordInput)

    def verCode(self):
        size = 10;
        chars = string.ascii_uppercase + string.digits
        return ''.join(random.choice(chars) for _ in range(size))

    def save(self, data):
        user = User()
        user.first_name = data['firstname']
        user.last_name = data['lastname']
        user.email = data['email']
        user.username = data['username']
        user.set_password(data['password'])
        user.save()

        useradd = Userextend()
        useradd.user_id = user.id
        useradd.dob = data['dob']
        useradd.vercode = self.verCode()
        useradd.save()

    def sendEmail(self):
        message = "Your verification code is "

        send_mail('Email verification', message, 'unknown.emlap@gmail.com',
        ['mr.pramod.mjn@gmail.com'], fail_silently=False)
            

