from django.urls import path

from mainapp.views import products

app_name = 'mainapp'

urlpatterns = [
    path('<int:pk>/', products, name='products'),
    path('', products, name='index'),

]
