from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Product

# Create your views here.
def home(request):
    return render(request, 'products/home.html')

def all_products(request):
    products = Product.objects.all()
    return render(request, 'products/allproducts.html', {'products':products})

def details(request, product_id):
    product= get_object_or_404(Product, pk=product_id)
    return render(request, 'products/details.html', {'product':product})

def index(request):
    return render(request, "index.html")


