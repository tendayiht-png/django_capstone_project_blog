from unittest import result

from django.shortcuts import render
from django.http import HttpResponse
from .forms import NameForm

# Create your views here.
def about_me(request):
    return HttpResponse("This would be the about page")

def home(request):
    return render(request, "index.html", {"name": "Guest"})

def add(request):
    val1 = int(request.GET['num1'])
    val2 = int(request.GET['num2'])
    res = val1 + val2
    return render(request, "index.html", {"result": res})





    

