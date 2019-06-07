from django.urls import path

import mainapp.views as mainapp

app_name = 'mainapp'

urlpatterns = [
    path('category/<int:pk>/', mainapp.products, name='category'),
    path('product/<int:pk>/', mainapp.product, name='product'),
    path('', mainapp.main, name='main')
]
