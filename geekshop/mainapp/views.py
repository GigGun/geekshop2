from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import ProductCategory, Product
from basketapp.models import BasketSlot

import random as rnd

context = {'title': 'Вагончик',
           'links_menu': {'main': 'Главная', 'products': 'Каталог', 'contact': 'Контакты'},
           'category': ProductCategory.objects.all(),
           'products': Product.objects.all(),
           }


def main(request):
    return render(request, 'mainapp/index.html', context)


def products(request, pk=None, page=1):

    basket = []
    if request.user.is_authenticated:
        basket = BasketSlot.objects.filter(user=request.user)

    total_quantity = sum(list(map(lambda basket_slot: basket_slot.quantity, basket)))
    print(total_quantity)

    title = 'продукты'
    links_menu = ProductCategory.objects.all()
    basket = get_basket(request.user)

    if pk is not None:
        if pk == 0:
            category = {
                'pk': 0,
                'name': 'все', }
            products_obj = Product.objects.filter(is_active=True,
                                                  category__is_active=True).\
                order_by('price')
        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            products_obj = Product.objects.filter(category__pk=pk,
                                                  is_active=True,
                                                  category__is_active=True).\
                order_by('price')

        paginator = Paginator(products, 2)
        try:
            products_paginator = paginator.page(page)
        except PageNotAnInteger:
            products_paginator = paginator.page(1)
        except EmptyPage:
            products_paginator = paginator.page(paginator.num_pages)

        context = {'title': title,
                   'links_menu': links_menu,
                   'category': category,
                   'products': products_paginator,
                   'basket': basket, }
        return render(request, 'mainapp/product_list.html', context)

    hot_product = get_hot_product()
    same_products = get_same_products(hot_product)

    context = {'title': title,
               'links_menu': links_menu,
               'hot_product': hot_product,
               'products': same_products,
               'basket': basket, }

    return render(request, 'mainapp/products.html', context)


def contact(request):
    return render(request, 'mainapp/contact.html', context)


def product(request, pk):
    title = 'продукты'

    context = {
        'title': title,
        'links_menu': ProductCategory.objects.all(),
        'product': get_object_or_404(Product, pk=pk),
        'basket': get_basket(request.user), }

    return render(request, 'mainapp/product.html', context)


def get_basket(user):
    if user.is_authenticated:
        return BasketSlot.objects.filter(user=user)
    else:
        return []


def get_hot_product():
    products = Product.objects.all()
    return rnd.sample(list(products), 1)[0]


def get_same_products(hot_product):
    same_products = Product.objects.filter(category=hot_product.category).\
                        exclude(pk=hot_product.pk)[:3]
    return same_products
