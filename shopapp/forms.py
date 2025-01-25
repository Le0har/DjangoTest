from django import forms
from django.core import validators
from .models import Product, Order
from django.contrib.auth.models import Group


# class ProductForm(forms.Form):
#     name = forms.CharField(label='Название', max_length=100)
#     price = forms.DecimalField(label='Цена', min_value=1, max_value=10000, decimal_places=2)
#     description = forms.CharField(
#         label='Описание товара', 
#         widget=forms.Textarea(attrs={'row': 5, 'cols': 30}),
#         validators=[validators.RegexValidator(
#             regex=r'новый',
#             message='Необходимо слово "новый"'
#         )]
#     )


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'description', 'discount']
        labels = {'name': 'Название', 'price': 'Цена', 'description': 'Описание товара', 'discount': 'Скидка'}


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['adress', 'promo', 'user', 'products']
        labels = {'adress': 'Адрес', 'promo': 'Промо-код', 'user': 'Клиент', 'products': 'Товары'}
        widgets = {
            'products': forms.CheckboxSelectMultiple(attrs={'class': 'form-control'}) 
        }


class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['name']
