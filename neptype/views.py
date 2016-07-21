from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from .forms import loginform, UserForm
from django.contrib.auth.models import User
from .models import Userextend
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def index(request):
    errorcheck = False
    context = {}
    if request.method == 'POST':
        form = UserForm(request.POST)

        if form.is_valid():
            '''user = User()
            user.first_name = form.cleaned_data['firstname']
            user.last_name = form.cleaned_data['lastname']
            user.email = form.cleaned_data['email']
            user.username = form.cleaned_data['username']
            user.set_password(form.cleaned_data['password'])
            user.save()

            useradd = Userextend()
            useradd.user_id = user.id
            useradd.dob = form.cleaned_data['dob']
            useradd.save()'''
            #form.sendEmail() 
            form.save(form.cleaned_data)
            return HttpResponseRedirect('/neptype/verify/')

    else:
        form = UserForm() #Display form with error message
        errorcheck = True

    context = {'form' : form, 'errorcheck' : errorcheck}
    return render(request, 'neptype/index.html', {'form': form})

def signin(request):
    context = {}
    return render(request, 'neptype/signin.html', context)

def home(request):
    if request.method == 'POST':
        usrname = request.POST['username']
        psword = request.POST['password']
        user = authenticate(username=usrname, password=psword)
        if user is not None:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect('/neptype/verify/')
                #return HttpResponse("Welcome %s" % user.first_name)
            else:
                return HttpResponseRedirect('/neptype/')
        else:
            return HttpResponseRedirect('/neptype/')

    #return HttpResponse("Going Good %s" % user.is_active)

def signup(request):
    context = {}
    if request.method == 'POST':
        form = UserForm(request.POST)

        if form.is_valid():
            '''user = User()
            user.first_name = form.cleaned_data['firstname']
            user.last_name = form.cleaned_data['lastname']
            user.email = form.cleaned_data['email']
            user.username = form.cleaned_data['username']
            user.set_password(form.cleaned_data['password'])
            user.save()

            useradd = Userextend()
            useradd.user_id = user.id
            useradd.dob = form.cleaned_data['dob']
            useradd.save()'''
            #form.sendEmail() 
            form.save(form.cleaned_data)
            return HttpResponseRedirect('/neptype/verify/')

    else:
        form = UserForm() #Display form with error message

    return render(request, 'neptype/signup.html', {'form': form})

def emailverify(request):
    if request.user.is_authenticated:
        user = request.user
    else:
        user = User.objects.get(pk=5)
    context = {'user' : user}
    return render(request, 'neptype/emailverify.html', context)

def signoff(request):
    logout(request)
    return HttpResponseRedirect('/neptype/')

def race(request):
    text = """This is a sample text to check whether it can be presented as the
    text for typing."""
    context={'text' : text}
    return render(request, 'neptype/race.html', context)

