# Generated by Django 3.1.7 on 2021-04-20 19:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_article_update_at'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='update_at',
            new_name='updated_at',
        ),
    ]
