from django.shortcuts import render,get_object_or_404
from .models import project_blog

def all_blog(request):
    blog_project = project_blog.objects.all()
    return render(request , 'blog/all_blog.html' , {'blog_project':blog_project})

def detail(request , blog_id):

    blog = get_object_or_404(project_blog , pk = blog_id)
    return render(request , 'blog/detail.html' , {'blog': blog})