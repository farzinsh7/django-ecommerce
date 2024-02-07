# Generated by Django 5.0.1 on 2024-02-06 12:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0034_product_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='variant',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='variant', to='product.product'),
        ),
    ]
