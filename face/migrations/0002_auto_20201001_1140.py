# Generated by Django 3.1.1 on 2020-10-01 11:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('face', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imagemodel',
            name='address',
        ),
        migrations.RemoveField(
            model_name='imagemodel',
            name='title',
        ),
    ]
