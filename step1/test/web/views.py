from django.shortcuts import render
from django.http import  HttpResponse
from  web.models import WebSite
from common.mymako import render_mako_context

import time
# Create your views here.
def index(request):
    return  HttpResponse('hello world!')
def sites(request):
    ctx={}
    obs=WebSite.objects.all()
    ctx['data']=obs
    return render_mako_context(request, "web/site.html", ctx)
def addSite(request):
    newSite = WebSite(name="baidu", url="http://www.baidu.com");
    newSite.save();
    return HttpResponse('ok!')
