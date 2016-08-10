import json
<<<<<<< HEAD
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Englishtext

def load_text(request):
    if request.is_ajax():
        english = Englishtext.objects.get(id=1)
        data = json.dumps(english.typing_text)
=======
import random
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Englishtext, Userextend

def load_text(request):
    info = []
    if request.is_ajax():
        if request.user.is_authenticated():
            usr = Userextend.objects.get(id=request.user.id)
            info.append(usr.eng_speed)
        else:
            data.append(0)
        id_num = random.randint(1,700)
        english = Englishtext.objects.get(id=id_num)
        info.append(english.typing_text)
        data = json.dumps(info)
>>>>>>> 37c339a605e48c23a3f69e3a9b297d9507e67a2b
        return HttpResponse(data, content_type='application/json')
        #return HttpResponseRedirect('/neptype/')
    else:
        raise Http404

<<<<<<< HEAD
=======
def update_speed(request):
    if request.is_ajax() and request.POST:
            d_data = None
            if request.user.is_authenticated():
                usr = Userextend.objects.get(id=request.user.id)
                usr.eng_speed = request.POST.get('new_speed')
                usr.save()
            data = json.dumps(d_data)
            return HttpResponse(data, content_type='application/json')
    else:
        raise Http404

>>>>>>> 37c339a605e48c23a3f69e3a9b297d9507e67a2b
