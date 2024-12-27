from django.core.management import BaseCommand
from shopapp.models import Product, Order
from django.contrib.auth.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write('Создание заказа')
        user = User.objects.get(username='user1')
        order, created = Order.objects.get_or_create(adress='Горького, 1', promo='sale', user=user)
        if created:
            self.stdout.write(f'Заказ {order} создан')
        order, created = Order.objects.get_or_create(adress='Маяковского, 25', promo='no-sale', user=user)
        if created:
            self.stdout.write(f'Заказ {order} создан')

        self.stdout.write(self.style.SUCCESS('Заказы созданы'))