import json
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
        return HttpResponse(data, content_type='application/json')
        #return HttpResponseRedirect('/neptype/')
    else:
        raise Http404

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

