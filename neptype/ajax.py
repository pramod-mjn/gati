import json
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Englishtext

def load_text(request):
    if request.is_ajax():
        english = Englishtext.objects.get(id=1)
        data = json.dumps(english.typing_text)
        return HttpResponse(data, content_type='application/json')
        #return HttpResponseRedirect('/neptype/')
    else:
        raise Http404

