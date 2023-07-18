from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Post
from .forms import CommentForm, ContactForm

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
    bid_form = CommentForm()
    return render(request, 'market/detail.html', {
        'post': post, 'bid_form': bid_form
    })

def add_bid(request, post_id):
    form = CommentForm(request.POST)
    if form.is_valid():
        new_bid = form.save(commit=False)
        new_bid.post_id = post_id
        new_bid.save()
    return redirect('detail', post_id=post_id)

def add_contact(request, comment_id, post_id):
    form = ContactForm(request.POST)
    if form.is_valid():
        new_contact = form.save(commit=False)
        new_contact.comment_id = comment_id
        new_contact.save()
    return redirect('detail', post_id=post_id)

class PostCreate(CreateView):
    model = Post
    fields = ['item', 'picture', 'description', 'price']

class PostUpdate(UpdateView):
    model = Post
    fields = ['item', 'picture', 'description', 'price']

class PostDelete(DeleteView):
    model = Post
    success_url = '/market'

