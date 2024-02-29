# Generated by Django 5.0.2 on 2024-02-28 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test1', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='starts_product_date',
        ),
        migrations.AddField(
            model_name='product',
            name='product_name',
            field=models.CharField(default='', max_length=150),
        ),
        migrations.AlterField(
            model_name='product',
            name='start_product_date',
            field=models.DateTimeField(),
        ),
    ]