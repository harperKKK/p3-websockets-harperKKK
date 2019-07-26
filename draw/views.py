from django.shortcuts import render
from django.utils.safestring import mark_safe
import json

def main(request):
    return render(request, 'draw/main.html', {})

def initial(request):
    return render(request,'draw/initial.html',{})
 
def onefeed(request):
    return render(request,'draw/onefeed.html',{})
  
def tabs(request):
    return render(request,'draw/tabs.html',{})

def large(request):
    return render(request,'draw/large.html',{})