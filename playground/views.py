from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# Views/view functions are request handlers

def say_hello(request):
    return HttpResponse("Hello World")

def say_hello_h1(request):
    return render(request, 'hello2.html', {'name':'gaurav'})