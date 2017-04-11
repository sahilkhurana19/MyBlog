from django.shortcuts import render, get_object_or_404
from .models import Post#, Tag
# Create your views here.

def index(request):
    latest_posts = Post.objects.order_by('-published_date')[:5]
    #tags = Tag.objects.all()
    context = {'latest_posts':latest_posts}#, 'tags':tags}
    return render(request, 'blog/index.html', context)

def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    context = {'post': post}
    return render(request, 'blog/detail.html', context)