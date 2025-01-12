from django.urls import path
from shopapp import views


app_name = 'shopapp'

urlpatterns = [
    path('', views.shop_index, name='index'),
    path('groups/', views.group_list, name='group-list'),
    path('products/', views.products_list, name='products-list'),
    path('products/create/', views.create_product, name='product-create'),
    path('orders/', views.orders_list, name='orders-list'),
    path('orders/create/', views.create_order, name='order-create'),
]