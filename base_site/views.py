from django.shortcuts import render

from freelance.models import Category

fopportunities = [
        {
            'img':'static/assets/img/custom-icon/job60.png',
            'title':'Разместить вакансию',
            'description':'Создайте свое бесплатное объявление о вакансии и начните получать предложения в течение нескольких часов'
        },
        {
            'img':'static/assets/img/custom-icon/frelancer60.png',
            'title':'Нанимайте фрилансеров',
            'description':'Создайте свое бесплатное объявление о вакансии и начните получать предложения в течение нескольких часов'
        },
        {
            'img':'static/assets/img/custom-icon/working60.png',
            'title':'Выполняйте работу',
            'description':'Создайте свое бесплатное объявление о вакансии и начните получать предложения в течение нескольких часов'
        },
        {
            'img':'static/assets/img/custom-icon/payment60.png',
            'title':'Совершайте безопасные платежи',
            'description':'Создайте свое бесплатное объявление о вакансии и начните получать предложения в течение нескольких часов'
        }
    ]

fopportunities2 = [
        {
            'img':'static/assets/img/categories/searchbase2.png',
            'title':' Возможности доступа',
            'description':'Наш маркетплейс предоставляет платформу для талантливых людей'
        },
        {
            'img':'static/assets/img/custom-icon/frelancer60.png',
            'title':'Повышенная видимость',
            'description':'Присоединяясь к нашему рынку'
        },
        {
            'img':'static/assets/img/custom-icon/working60.png',
            'title':'Доступ к талантам в разных областях',
            'description':'Наш маркетплейс предоставляет кураторский пул талантливых специалистов в разных областях '
        },
        {
            'img':'static/assets/img/custom-icon/payment60.png',
            'title':'Гарантия качества',
            'description':' Мы обеспечиваем тщательный процесс проверки талантов на нашем сайте.'
        }
    ]

why_choose_Us = [
    'Получите Высококачественную работу',
    'Придерживайтесь своего бюджетного сервиса',
    'Плати, когда будешь счастлив',
    # 'Плати, когда будешь счастлив'
]

# Create your views here.
def index(request):
    categories = Category.objects.all()[:8]

    context = {
        'categories':categories,
        'why_choose_Us':why_choose_Us,
        'fopportunities':fopportunities,
        'fopportunities2':fopportunities2
    }
    return render(request, 'index.html', context)