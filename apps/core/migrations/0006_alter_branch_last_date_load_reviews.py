# Generated by Django 4.1.2 on 2022-10-26 09:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_workday_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='branch',
            name='last_date_load_reviews',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 25, 23, 44, 23, 953151), verbose_name='Последняя дата загрузки отзывов'),
        ),
    ]