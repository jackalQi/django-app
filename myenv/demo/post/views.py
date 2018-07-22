from django.shortcuts import render, get_object_or_404, redirect
from . models import Post
from .forms import PostFrom
from django.utils import timezone
# Create your views here.


def get_posts(request):
    posts = Post.objects.all()
    return render(request, 'posts_list.html', {"posts": posts})


def get_post(request, pk):
    post = get_object_or_404(Post, id=pk)
    return render(request, 'post_detail.html', {"post": post})


def new_post(request):
    if request.method == "POST":
        form = PostFrom(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.post_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostFrom()
    return render(request, 'new_post.html', {"form": form})


def edit_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostFrom(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.post_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostFrom(instance=post)
        return render(request, 'edit_post.html', {"form": form})


def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()

    return redirect('post_list')





