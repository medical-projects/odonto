# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-07-10 08:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('odonto', '0003_auto_20180304_1926'),
    ]

    operations = [
        migrations.AddField(
            model_name='investigation',
            name='rhinovirus',
            field=models.CharField(blank=True, choices=[(b'pending', b'pending'), (b'positive', b'positive'), (b'negative', b'negative')], max_length=20),
        ),
    ]
