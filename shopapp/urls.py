from django.urls import path
from shopapp import views


app_name = 'shopapp'

urlpatterns = [
    path('', views.ShopIndexView.as_view(), name='index'),
    path('groups/', views.GroupsListView.as_view(), name='group-list'),
    path('products/', views.ProductListView.as_view(), name='products-list'),
    path('products/<int:pk>/', views.ProductDetailView.as_view(), name='product-details'),
    path('products/<int:pk>/update/', views.ProductUpdateView.as_view(), name='product-update'),
    path('products/<int:pk>/confirm-delete/', views.ProductDeleteView.as_view(), name='product-delete'),
    path('products/create/', views.ProductCreateView.as_view(), name='product-create'),
    path('orders/', views.OrderListView.as_view(), name='orders-list'),
    path('orders/create/', views.create_order, name='order-create'),
    path('orders/<int:pk>/', views.OrderDetailView.as_view(), name='orders-details'),
]