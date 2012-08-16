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

def technicalwriting(request):
    t = loader.get_template('technical-writing.html')
    c = Context({
    })
    return HttpResponse(t.render(c))

def investigativejournalismandnews(request):
    t = loader.get_template('investigative-journalism-and-news.html')
    c = Context({
    })
    return HttpResponse(t.render(c))

def marcommandtradepublications(request):
    t = loader.get_template('marcomm-and-trade-publications.html')
    c = Context({
    })
    return HttpResponse(t.render(c))

def artsentertainmentandlifestyle(request):
    t = loader.get_template('arts-entertainment-and-lifestyle.html')
    c = Context({
    })
    return HttpResponse(t.render(c))

def commentaryandcreativity(request):
    t = loader.get_template('commentary-and-creativity.html')
    c = Context({
    })
    return HttpResponse(t.render(c))

def resume(request):
    t = loader.get_template('resume.html')
    c = Context({
    })
    return HttpResponse(t.render(c))
