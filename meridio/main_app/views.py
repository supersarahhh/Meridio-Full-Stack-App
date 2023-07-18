from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Post

# posts = [
#     {'item': 'Desk', 'picture': 'assets/desk.jpeg', 'date': '7/10, 11:34AM', 'condition': 'used', 'description': '', 'price': '0' },
#     {'item': 'Samsung TV', 'picture': 'assets/TV.jpeg', 'date': '7/7, 1:23PM', 'condition': 'used', 'description': '', 'price': '200' },
#     {'item': 'Couch', 'picture': 'assets/Couch.jpeg', 'date': '7/9, 3:41PM', 'condition': 'Mint', 'description': '', 'price': '100' },
#     {'item': 'Refrigerator', 'picture': '', 'date': '7/11, 5:10PM', 'condition': 'Opened Box', 'description': '', 'price': '125' },
#     {'item': 'Headphones', 'picture': '', 'date': '7/13', 'condition': 'used', 'description': '', 'price': '50' },   
# ]
# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def market_index(request):
    return render(request, 'market/index.html', {
        'posts': Post.objects.all()
    })

class postCreate(CreateView):
  model = Post
  fields = '__all__'

class postUpdate(UpdateView):
  model = Post
  fields = []

class postDelete(DeleteView):
  model = Post
  success_url = '/posts'