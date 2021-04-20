# Generated by Django 3.1.7 on 2021-04-20 17:32

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0003_auto_20210417_1755'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='views',
            field=models.IntegerField(default=0, verbose_name='Просмотры'),
        ),
        migrations.AlterField(
            model_name='article',
            name='readers',
            field=models.ManyToManyField(blank=True, related_name='readed_articles', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
    ]