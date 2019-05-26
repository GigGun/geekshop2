from django.shortcuts import render
from django.shortcuts import get_object_or_404

from .models import ProductCategory, Product
from basketapp.models import BasketSlot

context = {'title': 'Вагончик',
           'links_menu': {'main': 'Главная', 'products': 'Каталог', 'contact': 'Контакты'},
           'category': ProductCategory.objects.all(),
           'products': Product.objects.all(),
           }


def main(request):
    return render(request, 'mainapp/index.html', context)


def products(request, pk=None):

    basket = []
    if request.user.is_authenticated():
        basket = BasketSlot.objects.filter(user=request.user)

    total_quatity = sum(list(map(lambda basket_slot: basket_slot.quantity, basket())))

    title = 'продукты'
    links_menu = ProductCategory.objects.all()

    if pk is not None:
        if pk == 0:
            products_obj = Product.objects.all().order_by('price')
            category = {'name': 'все'}

        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            products_obj = Product.objects.filter(category__pk=pk).order_by('price')

        context = {'title': title,
                   'links_menu': links_menu,
                   'category': category,
                   'products': products_obj,
                   'basket_quantity': total_quatity, }
        return render(request, 'mainapp/product_list.html', context)

    same_products = Product.objects.all()[1:3]

    context = {'title': title,
               'links_menu': links_menu,
               'products': same_products, }

    return render(request, 'mainapp/products.html', context)


def contact(request):
    return render(request, 'mainapp/contact.html', context)
