# Generated by Django 4.1.6 on 2023-03-05 11:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items_list', '0006_shoppinglist_greated_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='shoppinglist',
            name='is_public',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='shoppinglist',
            name='greated_at',
            field=models.DateField(default=datetime.datetime(2023, 3, 5, 13, 5, 50, 147814)),
        ),
    ]