# Generated by Django 2.0.13 on 2019-07-29 13:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('odonto_submissions', '0004_auto_20190729_1255'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='submission',
            options={'get_latest_by': 'submission_number'},
        ),
    ]