from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def hello_world(request):
    return render(request, 'base.html')
    #return HttpResponse("Hello world!")
