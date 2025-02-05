"""
В этом файле представления для интернет-магазина: товары, заказы.
"""

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.shortcuts import render, redirect, reverse, get_object_or_404
from timeit import default_timer
from django.contrib.auth.models import Group
from shopapp.models import Product, Order
from .forms import ProductForm, OrderForm, GroupForm
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from rest_framework.viewsets import ModelViewSet
from .serializers import ProductSerializer, OrderSerializer
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema, OpenApiResponse


@extend_schema(
    description='CRUD представление',
    tags=['Товары'],
    )
class ProductViewSet(ModelViewSet):
    """
    Набор представлений для модели Product
    Полный CRUD для сущности товара
    """

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [SearchFilter, DjangoFilterBackend, OrderingFilter]
    search_fields = ['name', 'description']
    ordering_fields = ['name', 'discount', 'price']
    filterset_fields = ['name', 'description', 'price', 'discount', 'archived', 'author']

    @extend_schema(
        summary='Получение продукта по ID',
        description='Более подробное описание...',
        responses={
            200: ProductSerializer,
            404: OpenApiResponse(description='Товар не найден, пустой запрос'),
        }
    )
    def retrieve(self, *args, **kwargs):
        return super().retrieve(*args, **kwargs)
    

class OrderViewSet(ModelViewSet):    
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class ShopIndexView(View):

    def get(self, request):
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


# def shop_index(request):
#     products = [
#         ('Планшет', 100),
#         ('Колонка', 500),
#         ('Телефон', 300),
#     ]

#     context = {
#         'time_running': default_timer(),
#         'products': products,
#     }
#     return render(request, 'shopapp/index.html', context=context)


# def group_list(request):
#     context = {
#         'groups': Group.objects.prefetch_related('permissions').all(),
#     }
#     return render(request, 'shopapp/group-list.html', context=context)


class GroupsListView(View):

    def get(self, request):
        context = {
            'form': GroupForm(),
            'groups': Group.objects.prefetch_related('permissions').all(),
        }
        return render(request, 'shopapp/group-list.html', context=context)
    
    def post(self, request):
        form = GroupForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect(request.path)


# def create_product(request):
#     if request.method == 'POST':
#         form = ProductForm(request.POST)
#         if form.is_valid():
#             # name = form.cleaned_data['name']
#             # price = form.cleaned_data['price']
#             # Product.objects.create(
#             #     name=name,
#             #     price=price
#             # )
#             # Product.objects.create(**form.cleaned_data)
#             form.save()
#             url = reverse('shopapp:products-list')
#             return redirect(url)
#     else:
#         form = ProductForm()
#     context = {
#         'form': form
#     }
#     return render(request, 'shopapp/create_product.html', context=context)


class ProductCreateView(CreateView):
    model = Product
    fields = ['name', 'price', 'description', 'discount']
    # form_class = ProductForm
    success_url = reverse_lazy('shopapp:products-list')


class ProductUpdateView(UpdateView):
    model = Product
    fields = ['name', 'price', 'description', 'discount']
    template_name_suffix = '_update'

    def get_success_url(self):
        return reverse('shopapp:product-details', kwargs={'pk': self.object.pk})


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('shopapp:products-list')

    def form_valid(self, form):
        success_url = self.get_success_url()
        self.object.archived = True
        self.object.save()
        return HttpResponseRedirect(success_url)


# def products_list(request):
#     context = {
#         'products': Product.objects.all(),
#     }
#     return render(request, 'shopapp/products-list.html', context=context)


class ProductListView(ListView):
    template_name = 'shopapp/products-list.html'
    # model = Product
    queryset = Product.objects.filter(archived=False)
    context_object_name = 'products'
    
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['products'] = Product.objects.all()
    #     return context


# class ProductDetailView(View):

#     def get(self, request, pk):
#         # product = Product.objects.get(pk=pk)
#         product = get_object_or_404(Product, pk=pk)
#         context = {
#             'product': product
#         }
#         return render(request, 'shopapp/products-details.html', context=context)


class ProductDetailView(DetailView):
    template_name = 'shopapp/products-details.html'
    model = Product
    context_object_name = 'product'


# def create_order(request):
#     if request.method == 'POST':
#         form = OrderForm(request.POST)
#         if form.is_valid():
#             form.save()
#             url = reverse('shopapp:orders-list')
#             return redirect(url)
#     else:
#         form = OrderForm()
#     context = {
#         'form': form
#     }
#     return render(request, 'shopapp/create_order.html', context=context)

# def orders_list(request):
#     context = {
#         'orders': Order.objects.all(),
#     }
#     return render(request, 'shopapp/orders-list.html', context=context)


class OrderListView(ListView, PermissionRequiredMixin):
    # model = Order
    permission_required = 'shopapp:view_order'
    queryset = Order.objects.all()


class OrderDetailView(DetailView):
    queryset = Order.objects.all()


class OrderCreateView(CreateView):
    form_class = OrderForm
    success_url = reverse_lazy('shopapp:orders-list')
    template_name = 'shopapp/create_order.html'


class OrderUpdateView(UpdateView):
    model = Order
    form_class = OrderForm
    template_name_suffix = '_update'

    def get_success_url(self):
        return reverse('shopapp:order-details', kwargs={'pk': self.object.pk})
    

class OrderDeleteView(DeleteView):
    model = Order
    template_name = 'shopapp/order_delete.html'
    success_url = reverse_lazy('shopapp:orders-list')
