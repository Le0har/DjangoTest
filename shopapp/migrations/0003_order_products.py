# Generated by Django 5.1.4 on 2024-12-21 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopapp', '0002_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='products',
            field=models.ManyToManyField(to='shopapp.product'),
        ),
    ]
