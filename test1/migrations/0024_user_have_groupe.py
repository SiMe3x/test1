# Generated by Django 5.0.2 on 2024-02-29 19:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test1', '0023_groupe_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_have_groupe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('groupe_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test1.groupe_product')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test1.user_have_product')),
            ],
        ),
    ]
