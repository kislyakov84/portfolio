from django.contrib import messages
from django.shortcuts import render
from .models import Project

def home(request):
    return render(request, 'portfolio/home.html')

def about(request):
    return render(request, 'portfolio/about.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
         # Логика обработки формы (например, сохранение или отправка email)
        print(f"Сообщение от {name} ({email}): {message}")
        messages.success(request, 'Ваше сообщение было отправлено!')
    return render(request, 'portfolio/contact.html')

def projects(request):
    projects_list = Project.objects.all()
    return render(request, 'portfolio/projects.html', {'projects': projects_list})