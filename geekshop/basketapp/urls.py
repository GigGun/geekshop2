from django.urls import path

from .views import basket, add, delete

app_name = 'basketapp'

urlpatterns = [
    path('', basket, name='view'),
    path('add/product/<int:pk>/', add, name='add'),
    path('delete/product/<int:pk>/', delete, name='delete'),
]
