from django.shortcuts import render, get_object_or_404

from .models import Blog

def allblogs(request):
    blog = Blog.objects
    return render(request, 'blog/allblogs.html', {'blog':blog})

def details(request, blog_id):
    blogdetail = get_object_or_404(Blog, pk = blog_id)
    return render(request, 'blog/blogdetail.html', {'blogdetail':blogdetail})