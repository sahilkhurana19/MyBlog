from django.shortcuts import render
from .models import Post
# Create your views here.

def index(request):
    latest_posts = Post.objects.order_by('-published_date')[:5]
    context = {'latest_posts':latest_posts}
    return render(request, 'blog/index.html', context)

def detail():
    pass