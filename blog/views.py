from django.shortcuts import render
from django.utils import timezone
from . models import Post

# Create your views here.

# create view for post_list.html
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')[:5]
    stuff_for_frontend = {'posts': posts} #creating context value
    return render(request, 'blog/post_list.html', stuff_for_frontend)
