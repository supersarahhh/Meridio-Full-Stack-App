from django.shortcuts import render


Posts = [
    {'name': 'Desk', 'pic': 'assets/desk.jpeg', 'datetime': '7/10, 11:34AM', 'condition': 'used', 'description': '', 'price': 'Free' },
    {'name': 'Samsung TV', 'pic': 'assets/TV.jpeg', 'datetime': '7/7, 1:23PM', 'condition': 'used', 'description': '', 'price': '$200' },
    {'name': 'Couch', 'pic': 'assets/Couch.jpeg', 'datetime': '7/9, 3:41PM', 'condition': 'Mint', 'description': '', 'price': '$100' },
    {'name': 'Refrigerator', 'pic': '', 'datetime': '7/11, 5:10PM', 'condition': 'Opened Box', 'description': '', 'price': '$125' },
    {'name': 'Headphones', 'pic': '', 'datetime': '7/13', 'condition': 'used', 'description': '', 'price': '$50' },   
]
# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def market_index(request):
    return render(request, 'market/index.html', {
        'items': items
    })