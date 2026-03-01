from unittest import result

from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import NameForm

# views.py
def home(request):
    return render(request, "index.html", {"name": "Guest"})

def add(request):
    val1 = int(request.GET['num1'])
    val2 = int(request.GET['num2'])
    res = val1 + val2
    return render(request, "index.html", {"result": res})

    

