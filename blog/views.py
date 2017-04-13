from django.shortcuts import render, get_object_or_404
from .models import Post, Tag
# Create your views here.

def index(request):
    latest_posts = Post.objects.order_by('-published_date')[:5]
    tags = Tag.objects.all()
    posts = Post.objects.all().order_by('-published_date')
    context = {'latest_posts':latest_posts, 'posts':posts, 'tags':tags}
    return render(request, 'blog/index.html', context)

def detail(request, post_id):
    latest_posts = Post.objects.order_by('-published_date')[:5]
    post = get_object_or_404(Post, pk=post_id)
    tags = Tag.objects.all()
    try:
        next_post = Post.objects.get(pk=int(post_id) + int(1))
    except:
        next_post = []
    try:
        previous_post = Post.objects.get(pk = int(post_id) - int(1) )
    except:
        previous_post = []
    context = {'post': post, 'tags':tags, 'latest_posts':latest_posts, 'next_post': next_post,'previous_post': previous_post}
    return render(request, 'blog/detail.html', context)

def category(request, tag_id):
    latest_posts = Post.objects.order_by('-published_date')[:5]
    posts = Post.objects.filter(tags__pk = tag_id ).order_by('-published_date')
    tags = Tag.objects.all()
    context = {'posts':posts, 'tags':tags, 'latest_posts': latest_posts}
    return render(request, 'blog/category.html', context)

def contact(request):
    latest_posts = Post.objects.order_by('-published_date')[:5]
    tags = Tag.objects.all()
    context = {'latest_posts':latest_posts, 'tags':tags}
    return render(request, 'blog/contact.html', context)