# Generated by Django 5.0.1 on 2024-02-05 10:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0011_remove_gallery_productvariation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productvariation',
            name='variation',
        ),
    ]