from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

tasks = [
    {
        'title': 'First Tasc',
        'text': 'Text tejasdf osjkds djgkd ghjgjhdf gjsdfkghfd gdfskljgh',
    }
]


def home(request):
    context = {
        'tasks': tasks
    }
    return render(request, 'TaskManager/home.html', context)


def about(request):
    return render(request, 'TaskManager/about.html', {'title': 'About'})
