# Generated by Django 5.0.1 on 2024-02-05 12:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0026_remove_variant_attribute_variant_variations'),
    ]

    operations = [
        migrations.CreateModel(
            name='VariantGallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('image', models.ImageField(blank=True, null=True, upload_to='shop/gallery')),
                ('variant', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='img', to='product.variant')),
            ],
        ),
    ]