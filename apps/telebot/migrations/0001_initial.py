# Generated by Django 4.1.2 on 2022-11-08 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TelebotSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tg_token', models.CharField(max_length=200, verbose_name='Токен')),
                ('tg_chat', models.CharField(max_length=200, verbose_name='Chat id')),
                ('is_admin_bot', models.BooleanField(default=False, verbose_name='Is admin bot')),
            ],
            options={
                'verbose_name': 'Настройка бота',
                'verbose_name_plural': 'Настройки ботов',
            },
        ),
    ]
