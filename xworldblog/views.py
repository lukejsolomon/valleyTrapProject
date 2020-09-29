from django.shortcuts import render, get_object_or_404
from .models import Blog


def all_blogs(request):
    blogs = Blog.objects.order_by('?')
    return render(request, 'xworldblog/all_blogs.html', {'blogs': blogs})


def all_blogsTail(request):
    blogs = Blog.objects.order_by('?')
    return render(request, 'xworldblog/all_blogsTail.html', {'blogs': blogs})


def Entertainment(request):
    blogs = Blog.objects.filter(category='Entertainment')
    return render(request, 'xworldblog/Entertainment.html', {'blogs': blogs})


def Technology(request):
    blogs = Blog.objects.filter(category='Technology')
    return render(request, 'xworldblog/Technology.html', {'blogs': blogs})


def Culture(request):
    blogs = Blog.objects.filter(category='Culture')
    return render(request, 'xworldblog/Culture.html', {'blogs': blogs})


def pageOne(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'xworldblog/pageOne.html', {'blog': blog})


def pageTwo(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'xworldblog/pageTwo.html', {'blog': blog})


def pageThree(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'xworldblog/pageThree.html', {'blog': blog})


def pageFour(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'xworldblog/pageFour.html', {'blog': blog})
