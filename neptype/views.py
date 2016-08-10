from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from .forms import loginform, UserForm
from django.contrib.auth.models import User
from .models import Userextend
from django.contrib.auth import authenticate, login, logout
# Create your views here.
<<<<<<< HEAD

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
=======
def get_speedyuser(score1, score2):
    query = "select * from neptype_userextend where\
    eng_speed between %s and %s order by eng_speed DESC limit 5"
    users = Userextend.objects.raw(query, [score1, score2])
    return users
    
def index(request):
    beginners = get_speedyuser(0,50)
    semipros = get_speedyuser(51,100)
    pros = get_speedyuser(101,200)
    context = {'beginners': beginners, 'semipros': semipros, 'pros': pros}
    if request.user.is_authenticated():
        c_user = Userextend.objects.get(id=request.user.id)
        context = {'beginners': beginners, 'semipros': semipros, 'pros': pros,
                'c_user': c_user}

        return render(request, 'neptype/index.html',context)
    else:
        return HttpResponseRedirect('/neptype/signin/')

def signin(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/neptype/')
    beginners = get_speedyuser(0,50)
    semipros = get_speedyuser(51,100)
    pros = get_speedyuser(101,200)
    context = {'beginners': beginners, 'semipros': semipros, 'pros': pros}
>>>>>>> 37c339a605e48c23a3f69e3a9b297d9507e67a2b
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
<<<<<<< HEAD
    context = {}
=======
>>>>>>> 37c339a605e48c23a3f69e3a9b297d9507e67a2b
    if request.method == 'POST':
        form = UserForm(request.POST)

        if form.is_valid():
<<<<<<< HEAD
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
=======
            #form.sendEmail() 
            form.save(form.cleaned_data)
            signup_error = False
            return HttpResponseRedirect('/neptype/verify/')

        else:
            form = UserForm() #Display form with error message

    beginners = get_speedyuser(0,50)
    semipros = get_speedyuser(51,100)
    pros = get_speedyuser(101,200)
    context = {'form': form, 'beginners': beginners, 'semipros': semipros, 'pros': pros}
    return render(request, 'neptype/signup.html',context)

def emailverify(request):
    if request.method=="POST":
        usr = Userextend.objects.get(id=request.user.id)
        if usr.vercode == request.POST["ver_code"]:
                usr.verified = 1
                usr.save()
    return HttpResponseRedirect('/neptype/')
>>>>>>> 37c339a605e48c23a3f69e3a9b297d9507e67a2b

def signoff(request):
    logout(request)
    return HttpResponseRedirect('/neptype/')

def race(request):
<<<<<<< HEAD
    text = """This is a sample text to check whether it can be presented as the
    text for typing."""
    context={'text' : text}
=======
    context = {}
    if request.user.is_authenticated():
        usr = Userextend.objects.get(id=request.user.id)
        context = {'max_speed': usr.eng_speed}
>>>>>>> 37c339a605e48c23a3f69e3a9b297d9507e67a2b
    return render(request, 'neptype/race.html', context)

