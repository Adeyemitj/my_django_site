from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from .form import PostForm, CommentForm
from .models import Post, Comment


# Create your views here.

# create a function to view all posts
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')[:5]
    stuff_for_frontend = {'posts': posts} #creating context value
    return render(request, 'blog/post_list.html', stuff_for_frontend)

# create a function to display post detail
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    stuff_for_frontend = {'post': post}
    return render(request, 'blog/post_detail.html', stuff_for_frontend)

# create a function to create new post
@login_required(login_url='/accounts/login')    # this retricts unauthorize access to the page
def post_new(request):
    # for form submission. create form, save and redirect to post_detail.html page. (Post request)
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():   # check if form contents are valid
            post = form.save(commit=False)  # save the new post but not committed to the database
            post.author = request.user      # take the user that login
            # post.published_date = timezone.now()
            post.save()  # save the the database
            return redirect('post_detail', pk=post.pk)  # save the post and redirect to the post detail page
    else:
        # to view post_edit.html page. Create new post (Get request)
        form = PostForm()
        stuff_for_frontend = {'form': form}
        return render(request, 'blog/post_edit.html', stuff_for_frontend)

# create a function to edit post
@login_required(login_url='/accounts/login')    # this retricts unauthorize access to the page
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        # updating an existing form
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            # post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        # show post edit form at the frontend
        form = PostForm(instance=post)
        stuff_for_frontend = {'form': form, 'post':post}
    return render(request, 'blog/post_edit.html', stuff_for_frontend)

# function to show all drafts post on the post_draft_list.html
@login_required(login_url='/accounts/login')    # this retricts unauthorize access to the page
def post_draft_list(request):
    posts = Post.objects.filter(published_date__isnull=True).order_by('-created_date')
    stuff_for_frontend ={'posts': posts}
    return render(request, 'blog/post_draft_list.html', stuff_for_frontend)

# function to publish draft post
@login_required(login_url='/accounts/login')    # this retricts unauthorize access to the page
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()       # this call the publish function in the model.py
    return redirect('post_detail', pk=pk)

# function to add comment
def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':    # this check if form method is POST
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)    # save only never commit
            comment.author = request.user
            comment.post = post
            comment.save()   # commit to database
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
        return render(request, 'blog/add_comment_to_post.html', {'form': form})

# function to delete comments from post
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('post_detail', pk=comment.post.pk)






