from django.urls import path
from shopapp import views


app_name = 'shopapp'

urlpatterns = [
    path('', views.shop_index, name='index'),
    path('groups/', views.group_list, name='group-list'),
    path('products/', views.products_list, name='products-list'),
    path('orders/', views.orders_list, name='orders-list'),
]