# Generated by Django 3.0.3 on 2020-04-13 06:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('negociospush', '0014_auto_20200412_1955'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notification',
            name='process',
        ),
    ]
