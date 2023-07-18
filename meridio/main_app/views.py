from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Post

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def market_index(request):
    posts = Post.objects.all()
    return render(request, 'market/index.html', {

        'posts': posts
    })

def market_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, 'market/detail.html', {
        'post': post
    })

class PostCreate(CreateView):
    model = Post
    fields = ['item', 'picture', 'description', 'price']

class PostUpdate(UpdateView):
    model = Post
    fields = ['item', 'picture', 'description', 'price']

class PostDelete(DeleteView):
    model = Post
    success_url = '/market'

