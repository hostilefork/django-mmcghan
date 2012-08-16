# Create your views here.

from django.template import Context, loader
from django.http import HttpResponse

def index(request):
    t = loader.get_template('index.html')
    c = Context({
	'value': '5'
    })
    return HttpResponse(t.render(c))

def techwriting(request):
    t = loader.get_template('techwriting.html')
    c = Context({
	'value': '5'
    })
    return HttpResponse(t.render(c))
