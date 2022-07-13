from django.shortcuts import render
from django.http import HttpResponse
from .models import Post, Tag


# Create your views here.
def posts_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/index.html', context={'posts' : posts})

def current_post(request, slug):
    post = Post.objects.get(slug__iexact=slug)
    return render(request, 'blog/current_post.html', context={'post' : post})

def tag_list(request):
    tags = Tag.objects.all()
    return render(request, 'blog/tag_list.html', context={'tags' : tags})

#def tag_detail(request, )