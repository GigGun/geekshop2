from django.urls import path

from .views import basket, add, delete, basket_edit

app_name = 'basketapp'

urlpatterns = [
    path('', basket, name='view'),
    path('add/product/<int:pk>/', add, name='add'),
    path('remove/product/<int:pk>/', delete, name='delete'),
    path('edit/<int:pk>/<int:quantity>/', basket_edit, name='edit'),
]
