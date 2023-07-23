from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('inventory/item/', views.inventory, name='inventory_item'),
    path('bakery/item/', views.bakery, name='bakery_item')
]