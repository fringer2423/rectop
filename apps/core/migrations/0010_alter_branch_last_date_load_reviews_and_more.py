# Generated by Django 4.1.2 on 2022-10-11 13:08

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_alter_branch_last_date_load_reviews_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='branch',
            name='last_date_load_reviews',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 11, 3, 8, 43, 633876), verbose_name='Последняя дата загрузки отзывов'),
        ),
        migrations.AlterField(
            model_name='branch',
            name='schedule',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.schedule', verbose_name='График работы'),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='friday',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='friday', to='core.workday', verbose_name='Пятница'),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='monday',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='monday', to='core.workday', verbose_name='Понедельник'),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='saturday',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='saturday', to='core.workday', verbose_name='Суббота'),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='sunday',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sunday', to='core.workday', verbose_name='Воскресенье'),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='thursday',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='thursday', to='core.workday', verbose_name='Четверг'),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='tuesday',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tuesday', to='core.workday', verbose_name='Вторник'),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='wednesday',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='wednesday', to='core.workday', verbose_name='Среда'),
        ),
    ]