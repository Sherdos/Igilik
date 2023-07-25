from django.shortcuts import render
from freelance.models import Category, Order

# Create your views here


def index(request):
    template_name = 'site/index.html'
    categories = Category.objects.all()
    context = {
        'categories':categories
    }
    return render(request,template_name,context)

def orders(request):
    template_name = 'site/orders.html'
    orders=Order.objects.all()
    categories = Category.objects.all()
    active_categories = request.POST.getlist('category')
    active_categories = list(map(int, active_categories))
    key_word = request.GET.get('key')
    if key_word:
        orders=Order.objects.filter(title__icontains = key_word)


        
    context = {
        'orders':orders,
        'categories':categories,
        'active_categories':active_categories
    }
    return render(request,template_name,context)


def category_view(request, id):
    template_name = 'site/category.html'
    categories = Category.objects.all()
    category = Category.objects.get(id=id)
    context = {
        'category':category,
        'categories':categories,
    }
    return render(request,template_name,context)

def category_filter(request):
    template_name = 'site/category.html'
    categories = request.POST.get('categories')
    context = {
        'categories':categories,
    }
    return render(request,template_name,context)
