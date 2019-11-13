from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from . models import Post

# Create your views here.

# create view for post_list.html
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')[:5]
    stuff_for_frontend = {'posts': posts} #creating context value
    return render(request, 'blog/post_list.html', stuff_for_frontend)

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    stuff_for_frontend = {'post': post}
    return render(request, 'blog/post_detail.html', stuff_for_frontend)
