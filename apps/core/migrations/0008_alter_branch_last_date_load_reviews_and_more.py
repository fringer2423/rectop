# Generated by Django 4.1.2 on 2022-10-11 12:21

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_workday_remove_schedule_friday_day_off_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='branch',
            name='last_date_load_reviews',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 11, 2, 20, 55, 581376), verbose_name='Последняя дата загрузки отзывов'),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='friday',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='friday', to='core.workday', verbose_name='Пятница'),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='monday',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='monday', to='core.workday', verbose_name='Понедельник'),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='saturday',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='saturday', to='core.workday', verbose_name='Суббота'),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='sunday',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='sunday', to='core.workday', verbose_name='Воскресенье'),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='thursday',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='thursday', to='core.workday', verbose_name='Четверг'),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='tuesday',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='tuesday', to='core.workday', verbose_name='Вторник'),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='wednesday',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='wednesday', to='core.workday', verbose_name='Среда'),
        ),
    ]