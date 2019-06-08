from django.urls import path

from .views import basket, add, basket_remove, basket_edit

app_name = 'basketapp'

urlpatterns = [
    path('', basket, name='view'),
    path('add/product/<int:pk>/', add, name='add'),
    path('remove/product/<int:pk>/', basket_remove, name='remove'),

    path('edit/<int:pk>/<int:quantity>/', basket_edit, name='edit'),
]
