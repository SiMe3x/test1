# Generated by Django 5.0.2 on 2024-02-29 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test1', '0016_remove_lesson_product_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='max_users',
            field=models.PositiveIntegerField(default=3),
        ),
        migrations.AlterField(
            model_name='product',
            name='min_users',
            field=models.PositiveIntegerField(default=2),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
