# Generated by Django 3.0.5 on 2020-04-27 14:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('GGuide', '0021_auto_20200427_1449'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='user_img',
        ),
    ]
