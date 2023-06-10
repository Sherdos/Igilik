from django.shortcuts import render
from freelance.models import Service, Category, Order

# Create your views here


def index(request):
    template_name = 'site/index.html'
    context = {

    }
    return render(request,template_name,context)

def services(request):
    orders=Order.objects.all()
    categories = Category.objects.all()
    template_name = 'site/services.html'
    context = {
        'orders':orders,
        'categories':categories
    }
    return render(request,template_name,context)

def search(request):
    key_word = request.GET.get('key')
    template_name = 'site/services.html'
    if key_word:
        orders=Order.objects.filter(title__icontains = key_word)
    context = {
        'orders':orders
    }
    return render(request,template_name,context)
