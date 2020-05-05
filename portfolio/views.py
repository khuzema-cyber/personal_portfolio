from django.shortcuts import render
from .models import project
from .models import project2

# Create your views here.
def home(request):
    projects = project.objects.all()
    return render(request , 'portfolio/home.html' , {'projects':projects})

def home2(request):
    project_two = project2.objects.all()

    return render(request , 'portfolio/home2.html' , {'project_two':project_two})