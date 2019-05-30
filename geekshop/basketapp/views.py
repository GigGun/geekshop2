from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from .models import BasketSlot
from mainapp.models import Product


def basket(request):
    title = 'корзина'
    basket_items = BasketSlot.objects.filter(user=request.user).\
        order_by('product__category')

    context = {
        'title': title,
        'basket_items': basket_items, }

    return render(request, 'basketapp/basket.html', context)


def basket_remove(request, pk):
    basket_record = get_object_or_404(BasketSlot, pk=pk)
    basket_record.delete()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def add(request, pk=None):
    product = get_object_or_404(Product, pk=pk)

    basket_slot_old = BasketSlot.objects.filter(product=product).first()

    if basket_slot_old:
        basket_slot_old.quantity += 1
        basket_slot_old.save()
    else:
        basket_slot = BasketSlot(product=product, user=request.user)
        basket_slot.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def delete(request, pk=None):
    product = get_object_or_404(Product, pk=pk)
    basket_slot = BasketSlot.objects.filter(product=product).first()

    if basket_slot:
        if basket_slot.quantity > 1:
            basket_slot.quantity -= 1
            basket_slot.save()
        else:
            basket_slot.delete()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
