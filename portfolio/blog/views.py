from django.shortcuts import render, get_object_or_404
from .models import Blog

# Create your views here.
def allblogs(request):
    allblogs = Blog.objects
    return render(request, 'blogs/home.html', {'blogs':allblogs})


def detail(request, blog_id):
    detail_blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog':detail_blog})
