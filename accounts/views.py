from django.shortcuts import render, redirect, HttpResponseRedirect, reverse
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import auth
from products.models import Product
from products.views import all_products


# Create your views here.
def success(request):
    return render(request, 'accounts/success.html')

def signup(request):
    if request.method=='POST':
        if request.POST['password1']==request.POST['password2']:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'accounts/signup.html', {'error':'username already taken'})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                auth.login(request,user)
                products = Product.objects.all()
                return redirect(reverse('success'))
        else:
            return render(request, 'accounts/signup.html', {'error':'passwords do not match'})

    else:
        return render(request, 'accounts/signup.html')


def login(request):
    if request.method=='POST':
        user=auth.authenticate(username=request.POST['username'],password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            products = Product.objects.all()
            return redirect(reverse('success'))
        else:
            return render(request, 'accounts/login.html', {'error':'Username or Password is incorrect'})
    else:
        return render(request, 'accounts/login.html')


def logout(request):
    auth.logout(request)
    return render(request, 'accounts/logout.html')
