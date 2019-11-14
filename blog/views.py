from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from .form import PostForm
from .models import Post

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

def post_new(request):
    # for form submission. create form, save and redirect to post_detail.html page. (Post request)
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid(): # check if form contents are valid
            post = form.save(commit=False)  # save the new post but not committed to the database
            post.author = request.user      # take the user that login
            post.published_date = timezone.now()
            post.save()  # save the the database
            return redirect('post_detail', pk=post.pk)  # save the post and redirect to the post detail page
    else:
        # to view post_edit.html page. Create new post (Get request)
        form = PostForm()
        stuff_for_frontend = {'form': form}
        return render(request, 'blog/post_edit.html', stuff_for_frontend)
