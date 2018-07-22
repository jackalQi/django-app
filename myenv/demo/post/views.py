from django.shortcuts import render, get_object_or_404
from . models import Post
# Create your views here.


def get_posts(request):
    posts = object.Post.all()
    return render(request, 'posts_list.html', {"posts": posts})

def get_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'post_detail.html', {"post": post})



