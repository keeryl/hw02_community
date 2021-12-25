from django.shortcuts import render, get_object_or_404
from .models import Post, Group


# Главная страница
def index(request):
    posts = Post.objects.order_by('-pub_date')[:10]
    template = '../templates/posts/index.html'
    context = {
        'posts': posts,
    }
    return render(request, template, context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    template = '../templates/posts/group_list.html'
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]
    text = 'просто текст'
    context = {
        'text': text,
        'group': group,
        'posts': posts,
    }
    return render(request, template, context)
