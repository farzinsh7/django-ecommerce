# Generated by Django 5.0.1 on 2024-02-06 06:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0028_delete_variantgallery'),
    ]

    operations = [
        migrations.CreateModel(
            name='GalleryVariations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('image', models.ImageField(blank=True, null=True, upload_to='shop/gallery')),
                ('variant', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='gallery_variations', to='product.variant')),
            ],
        ),
    ]