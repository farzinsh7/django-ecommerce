# Generated by Django 5.0.1 on 2024-02-13 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attribute', '0003_beltsize'),
        ('product', '0002_rename_regular_price_product_price_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='color',
            field=models.ManyToManyField(related_name='color', to='attribute.color'),
        ),
    ]
