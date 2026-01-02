from django.shortcuts import render
from .models import Project
# Create your views here.
def home(request):
    # This points to templates/portfolio/index.html
    return render(request, 'portfolio/HomePage.html')


def game_projects(request):
    # Fetch only projects where category is 'GAME'
    projects = Project.objects.filter(category='GAME') 
    return render(request, 'portfolio/game_projects.html', {'projects': projects})

def data_projects(request):
    # Fetch only projects where category is 'DATA'
    projects = Project.objects.filter(category='DATA')
    return render(request, 'portfolio/data_projects.html', {'projects': projects})

def web_projects(request):
    # Fetch only projects where category is 'WEB'
    projects = Project.objects.filter(category='WEB')
    return render(request, 'portfolio/web_projects.html', {'projects': projects})