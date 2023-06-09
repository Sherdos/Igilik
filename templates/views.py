from django.shortcuts import render
from freelance.models import Service, Category

# Create your views here


def index(request):
    services=Service.objects.all()
    categories = Category.objects.all()
    template_name = 'site/index.html'
    context = {
        'services':services,
        'categories':categories
    }
    return render(request,template_name,context)


def search(request):
    key_word = request.GET.get('key')
    template_name = 'site/index.html'
    if key_word:
        services=Service.objects.filter(title__icontains = key_word)
    context = {
        'services':services
    }
    return render(request,template_name,context)
