from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def hello(request, anything):
    return HttpResponse(f"<h1>Potato Wars are {anything}?<h1>")

def hello2(request):
    anything = request.GET.get("situation")
    return HttpResponse(f"<h1>Potato Wars are {anything}?<h1>")