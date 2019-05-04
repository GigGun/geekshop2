from django.shortcuts import render

from .models import ProductCategory, Product

context = {'title': 'Вагончик',
           'links_menu': {'main': 'Главная', 'products': 'Каталог', 'contact': 'Контакты'},
           'categories': ProductCategory.objects.all(),
           'products': Product.objects.all(),
           }


def main(request):
    return render(request, 'mainapp/index.html', context)


def products(request, pk=None):
    print(pk)
    return render(request, 'mainapp/products.html', context)


def contact(request):
    return render(request, 'mainapp/contact.html', context)
