# Generated by Django 5.0.2 on 2024-02-28 23:15

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('test1', '0004_remove_product_author_delete_lesson_delete_product'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(default='', max_length=150)),
                ('start_product_date', models.DateTimeField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lesson_name', models.CharField(default='', max_length=150)),
                ('lesson_link', models.SlugField(max_length=300, unique=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test1.product')),
            ],
        ),
    ]