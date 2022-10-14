# Generated by Django 4.1.2 on 2022-10-13 13:01

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_alter_branch_last_date_load_reviews_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reviewsettings',
            name='branch',
        ),
        migrations.AddField(
            model_name='reviewsettings',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='review_settings', to='core.company', verbose_name='Компания'),
        ),
        migrations.AlterField(
            model_name='branch',
            name='last_date_load_reviews',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 13, 3, 1, 0, 474417), verbose_name='Последняя дата загрузки отзывов'),
        ),
    ]