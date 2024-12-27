from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from timeit import default_timer
from django.contrib.auth.models import Group
from shopapp.models import Product, Order


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

def products_list(request):
    context = {
        'products': Product.objects.all(),
    }
    return render(request, 'shopapp/products-list.html', context=context)

def orders_list(request):
    context = {
        'orders': Order.objects.all(),
    }
    return render(request, 'shopapp/orders-list.html', context=context)