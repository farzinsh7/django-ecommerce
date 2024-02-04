# Generated by Django 5.0.1 on 2024-01-31 11:17

import ckeditor_uploader.fields
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('description', ckeditor_uploader.fields.RichTextUploadingField()),
                ('image', models.ImageField(upload_to='articles')),
                ('thumbnail', models.ImageField(null=True, upload_to='articles/thumb')),
                ('publish', models.DateTimeField(default=django.utils.timezone.now)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('d', 'Draft'), ('p', 'Publish')], max_length=1)),
                ('keywords', models.CharField(max_length=300, null=True)),
                ('seo_description', models.TextField(null=True)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='articles', to=settings.AUTH_USER_MODEL)),
                ('category', models.ManyToManyField(related_name='articles', to='article.category')),
                ('tags', models.ManyToManyField(blank=True, related_name='articles', to='article.tags')),
            ],
        ),
        migrations.DeleteModel(
            name='News',
        ),
    ]