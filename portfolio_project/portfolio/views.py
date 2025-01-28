from django.shortcuts import render
from .models import Project

def home(request):
    return render(request, 'portfolio/home.html')

def about(request):
    return render(request, 'portfolio/about.html')

def contact(request):
    return render(request, 'portfolio/contact.html')

def projects(request):
    projects_list = Project.objects.all()
    return render(request, 'portfolio/projects.html', {'projects': projects_list})