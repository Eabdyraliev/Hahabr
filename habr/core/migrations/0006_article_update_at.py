# Generated by Django 3.1.7 on 2021-04-20 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20210421_0052'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='update_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
