from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.core.handlers.wsgi import WSGIRequest

def home(request: WSGIRequest):
    return render(request, 'home.html')

def timer(request: WSGIRequest):
    return render(request, 'timer.html')

def contact(request: WSGIRequest):
    return render(request, 'contact.html')

def calculator(request: WSGIRequest):
    return render(request, 'calculator.html')

def calendar(request: WSGIRequest):
    return render(request, 'calendar.html')

def webhook(request: WSGIRequest):
    return render(request, 'webhook.html')

def countdown(request: WSGIRequest):
    return render(request, 'countdown.html')

def colorGenerator(request: WSGIRequest):
    return render(request, 'color-generator.html')

def screenSize(request: WSGIRequest):
    return render(request, 'screenSize.html')

def showPicture(request: WSGIRequest):
    return render(request, 'show-picture.html')