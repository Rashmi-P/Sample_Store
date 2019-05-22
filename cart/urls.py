from django.conf.urls import url
from .views import view_cart, add_to_cart, adjust_cart
from . import views
from django.urls import path
 
 
urlpatterns = [
    path('', views.view_cart, name='view_cart'),
    path('<int:product_id>/add_to_cart', views.add_to_cart, name='add_to_cart'),
    path('<int:product_id>/adjust_cart', views.adjust_cart, name='adjust_cart'),
]

