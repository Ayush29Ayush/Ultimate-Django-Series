# Generated by Django 5.0.6 on 2024-06-26 12:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0011_alter_order_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customer',
            options={'ordering': ['user__first_name', 'user__last_name'], 'permissions': [('view_history', 'Can View History')]},
        ),
    ]
