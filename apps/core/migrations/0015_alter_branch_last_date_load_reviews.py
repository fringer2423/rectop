# Generated by Django 4.1.2 on 2022-10-26 10:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_alter_branch_last_date_load_reviews'),
    ]

    operations = [
        migrations.AlterField(
            model_name='branch',
            name='last_date_load_reviews',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 26, 0, 43, 41, 720681), verbose_name='Последняя дата загрузки отзывов'),
        ),
    ]