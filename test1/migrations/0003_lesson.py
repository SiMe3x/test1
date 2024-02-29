# Generated by Django 5.0.2 on 2024-02-28 23:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test1', '0002_remove_product_starts_product_date_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('product', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='test1.product')),
                ('lesson_name', models.CharField(default='', max_length=150)),
                ('lesson_link', models.SlugField(max_length=300, unique=True)),
            ],
        ),
    ]