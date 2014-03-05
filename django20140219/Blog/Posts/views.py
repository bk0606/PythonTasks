from django.shortcuts import render
from Posts.models import Post

def PostsView(request):
    posts = Post.objects.all()
    return render(
        request,
        'posts/Posts.html',
        {'posts': posts}
    )

def PostView(request, id):
    post = Post.objects.get(id=id)
    return render(
        request,
        'posts/Post.html',
        {'post': post}
    )