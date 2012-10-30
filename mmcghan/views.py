# Create your views here.

from django.template import Context, loader
from django.http import HttpResponse

def index(request):
    t = loader.get_template('index.html')
    c = Context({
    # pass values to template from code, for instance:
	# 'value': '5'
    })
    return HttpResponse(t.render(c))

def technical(request):
    t = loader.get_template('technical.html')
    c = Context({
    })
    return HttpResponse(t.render(c))

def journalism(request):
    t = loader.get_template('journalism.html')
    c = Context({
    })
    return HttpResponse(t.render(c))

def marketing(request):
    t = loader.get_template('marketing.html')
    c = Context({
    })
    return HttpResponse(t.render(c))

def entertainment(request):
    t = loader.get_template('entertainment.html')
    c = Context({
    })
    return HttpResponse(t.render(c))

def creative(request):
    t = loader.get_template('creative.html')
    c = Context({
    })
    return HttpResponse(t.render(c))

def commentary(request):
    t = loader.get_template('commentary.html')
    c = Context({
    })
    return HttpResponse(t.render(c))

def poker_gallery(request):
    t = loader.get_template('gallery.html')
    c = Context({
    	'backgroundcolor': 'FF0000'
    })
    return HttpResponse(t.render(c))

def xxx(request):
    t = loader.get_template('base.html')
    c = Context({
    })
    return HttpResponse(t.render(c))

