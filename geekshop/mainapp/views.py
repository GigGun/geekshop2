from django.shortcuts import render
from django.shortcuts import get_object_or_404

from .models import ProductCategory, Product


context = {'title': 'Вагончик',
           'links_menu': {'main': 'Главная', 'products': 'Каталог', 'contact': 'Контакты'},
           'categories': ProductCategory.objects.all(),
           'products': Product.objects.all(),
           }


def main(request):
    return render(request, 'mainapp/index.html', context)


def products(request, pk=None):
    print(f'pk={pk}')

    title = 'продукты'
    links_menu = ProductCategory.objects.all()

    if pk is not None:
        print(f'pk={pk} True')
        if pk == 0:
            products_obj = Product.objects.all().order_by('price')
            category = {'name': 'все'}
        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            products_obj = Product.objects.filter(category__pk=pk).order_by('price')

        context = {'title': title,
                   'links_menu': links_menu,
                   'category': category,
                   'products': products_obj, }
        return render(request, 'mainapp/product_list.html', context)

    same_products = Product.objects.all()[1:3]
    print(f'same_products={same_products}')

    context = {'title': title,
               'links_menu': links_menu,
               'products': same_products, }

    return render(request, 'mainapp/products.html', context)


def contact(request):
    return render(request, 'mainapp/contact.html', context)
