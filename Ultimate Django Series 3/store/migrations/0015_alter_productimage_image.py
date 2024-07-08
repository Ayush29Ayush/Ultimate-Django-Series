# Generated by Django 5.0.6 on 2024-07-08 10:49

import store.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0014_productimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productimage',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='store/images', validators=[store.validators.validate_file_size]),
        ),
    ]
