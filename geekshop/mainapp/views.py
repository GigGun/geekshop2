from django.shortcuts import render

# Create your views here.


def main(request):
    context = {'title': 'Вагончик'}
    return render(request, 'mainapp/index.html', context)


def products(request):
    return render(request, 'mainapp/products.html')


def contact(request):
    return render(request, 'mainapp/contact.html')
