# Generated by Django 2.0.13 on 2019-12-06 14:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('odonto', '0023_auto_20191105_1114'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='investigation',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='investigation',
            name='episode',
        ),
        migrations.RemoveField(
            model_name='investigation',
            name='updated_by',
        ),
        migrations.DeleteModel(
            name='Investigation',
        ),
    ]