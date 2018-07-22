from django.shortcuts import render, get_object_or_404
from . models import Post
# Create your views here.


def get_posts(request):
    posts = Post.objects.all()
    return render(request, 'posts_list.html', {"posts": posts})


def get_post(request, pk):
    post = get_object_or_404(Post, id=pk)
    return render(request, 'post_detail.html', {"post": post})



