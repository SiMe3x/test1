# Generated by Django 5.0.2 on 2024-02-29 18:09

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test1', '0011_alter_user_have_product_product_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_have_product',
            name='product',
        ),
        migrations.AddField(
            model_name='product',
            name='have_access',
            field=models.ManyToManyField(to='test1.user_have_product'),
        ),
        migrations.AlterField(
            model_name='user_have_product',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
