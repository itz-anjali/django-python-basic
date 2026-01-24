from django.shortcuts import render 
from django.http import HttpResponse

def index(request):
    # return HttpResponse("<h1>Welcome to Home App! Working Successfully.</h1>")
      return render(request , 'index.html')


def about(request):
    return HttpResponse("<h1>Welcome to about App! Working Successfully.</h1>")

def contact(request):
    return HttpResponse("<h1>Welcome to contatc App! Working Successfully.</h1>")