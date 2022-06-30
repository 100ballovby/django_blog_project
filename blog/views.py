from django.shortcuts import render
from .models import Post
# Create your views here.


def posts(request):
    posts = Post.objects.filter(published=True).order_by('-created_at')
    # ^ достаю все посты из базы данных и закидываю их в список
    return render(request, 'index.html', {'posts': posts})
