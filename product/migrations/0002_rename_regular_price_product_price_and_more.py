# Generated by Django 5.0.1 on 2024-02-13 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='regular_price',
            new_name='price',
        ),
        migrations.RemoveField(
            model_name='product',
            name='sale_price',
        ),
        migrations.RemoveField(
            model_name='product',
            name='stock_quantity',
        ),
        migrations.AddField(
            model_name='product',
            name='status',
            field=models.CharField(choices=[('d', 'Draft'), ('p', 'Publish')], max_length=1, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='variation',
            field=models.CharField(choices=[('c', 'Color'), ('s', 'Size')], max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='dimenstions',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='sku',
            field=models.CharField(blank=True, max_length=200, null=True, unique=True),
        ),
    ]
