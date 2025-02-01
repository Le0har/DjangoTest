from django.urls import path, include
from shopapp import views
from rest_framework.routers import DefaultRouter


app_name = 'shopapp'

router = DefaultRouter()
router.register('products', views.ProductViewSet)
router.register('orders', views.OrderViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('', views.ShopIndexView.as_view(), name='index'),
    path('groups/', views.GroupsListView.as_view(), name='group-list'),
    path('products/', views.ProductListView.as_view(), name='products-list'),
    path('products/<int:pk>/', views.ProductDetailView.as_view(), name='product-details'),
    path('products/<int:pk>/update/', views.ProductUpdateView.as_view(), name='product-update'),
    path('products/<int:pk>/confirm-delete/', views.ProductDeleteView.as_view(), name='product-delete'),
    path('products/create/', views.ProductCreateView.as_view(), name='product-create'),
    path('orders/', views.OrderListView.as_view(), name='orders-list'),
    path('orders/create/', views.OrderCreateView.as_view(), name='order-create'),
    path('orders/<int:pk>/', views.OrderDetailView.as_view(), name='order-details'),
    path('orders/<int:pk>/update/', views.OrderUpdateView.as_view(), name='order-update'),
    path('orders/<int:pk>/delete/', views.OrderDeleteView.as_view(), name='order-delete'),
]