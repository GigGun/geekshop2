from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from .models import BasketSlot
from mainapp.models import Product


def add(request, pk=None):
    product = get_object_or_404(Product, pk=pk)

    basket_slot = BasketSlot(product=product, user=request.user)
    basket_slot.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def delete(request, pk=None):
    context = {}
    return render(request, 'basketapp/basket.html', context)
