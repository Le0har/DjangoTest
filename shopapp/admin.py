from django.contrib import admin
from .admin_mixins import Export_goods_mixin
from .models import Product, Order
from django.http import HttpRequest
from django.db.models import QuerySet


class OrderInline(admin.TabularInline):
    model = Product.orders.through


@admin.action(description='Безопасное удаление')
def mark_archived(modeladmin, request, queryset):
    queryset.update(archived=True)


@admin.action(description='Восстановление')
def mark_unarchived(modeladmin, request, queryset):
    queryset.update(archived=False)

@admin.action(description='Cкидка 0 -> 5 проц')
def make_discount(modeladmin, request, queryset):
    if queryset.filter(discount=0):
        queryset.update(discount=5)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin, Export_goods_mixin):
    actions = [mark_archived, mark_unarchived, make_discount, 'export_csv']
    inlines = [OrderInline]
    list_display = 'pk', 'name', 'description_short', 'price', 'discount', 'archived'
    list_display_links = 'pk', 'name'
    ordering = ['pk']
    search_fields = 'name', 'description'
    fieldsets = [
        (None, {
            'fields': ('name', 'description')
        }),
        ('Настройка цены', {
            'fields': ('price', 'discount'),
            'classes': ('collapse',)
        }),
        ('Дополнительные опции', {
            'fields': ('archived',),
            'classes': ('collapse',),
            'description': 'Безопасное удаление'
        }),
    ]

    def description_short(self, obj):
        if len(obj.description) < 50:
            return obj.description
        return obj.description[:50] + '...'
    

class ProductInline(admin.TabularInline):
    model = Order.products.through


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [ProductInline]
    list_display = 'pk', 'adress', 'promo', 'created_at', 'user_name'
    list_display_links = 'pk', 'adress'

    def get_queryset(self, request):
        return Order.objects.select_related('user')
    
    def user_name(self, obj):
        return obj.user.first_name or obj.user.username


#admin.site.register(Product, ProductAdmin)
