from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render

# Create your views here.

def index(request, *args, **kwargs):
  return render(request, 'client/index.html')

def handler404(request, *args, **kwargs):
    return HttpResponseRedirect('/')