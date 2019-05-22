from django.conf.urls import url, include
from django.urls import path
from . import views

urlpatterns = [
    path('products', views.all_products, name='products'),
    path('index', views.index, name='index'),
    path('<int:product_id>', views.details, name='details'),
    ]


