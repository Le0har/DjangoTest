from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect, reverse
from timeit import default_timer
from django.contrib.auth.models import Group
from shopapp.models import Product, Order
from .forms import ProductForm, OrderForm


def shop_index(request):
    products = [
        ('Планшет', 100),
        ('Колонка', 500),
        ('Телефон', 300),
    ]

    context = {
        'time_running': default_timer(),
        'products': products,
    }
    return render(request, 'shopapp/index.html', context=context)

def group_list(request):
    context = {
        'groups': Group.objects.prefetch_related('permissions').all(),
    }
    return render(request, 'shopapp/group-list.html', context=context)

def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            # name = form.cleaned_data['name']
            # price = form.cleaned_data['price']
            # Product.objects.create(
            #     name=name,
            #     price=price
            # )
            # Product.objects.create(**form.cleaned_data)
            form.save()
            url = reverse('shopapp:products-list')
            return redirect(url)
    else:
        form = ProductForm()
    context = {
        'form': form
    }
    return render(request, 'shopapp/create_product.html', context=context)

def products_list(request):
    context = {
        'products': Product.objects.all(),
    }
    return render(request, 'shopapp/products-list.html', context=context)

def create_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            url = reverse('shopapp:orders-list')
            return redirect(url)
    else:
        form = OrderForm()
    context = {
        'form': form
    }
    return render(request, 'shopapp/create_order.html', context=context)

def orders_list(request):
    context = {
        'orders': Order.objects.all(),
    }
    return render(request, 'shopapp/orders-list.html', context=context)