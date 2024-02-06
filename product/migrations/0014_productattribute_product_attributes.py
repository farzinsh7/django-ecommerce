# Generated by Django 5.0.1 on 2024-02-05 10:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attribute', '0005_remove_attribute_product'),
        ('product', '0013_remove_product_attributes_delete_productvariation'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductAttribute',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attribute', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='attribute.attribute')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='attributes',
            field=models.ManyToManyField(blank=True, null=True, through='product.ProductAttribute', to='attribute.attribute'),
        ),
    ]