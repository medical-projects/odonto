# Generated by Django 2.0.13 on 2019-07-24 09:58

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('odonto_submissions', '0008_auto_20190724_0821'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompassBatchResponse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('content', models.TextField(default='')),
                ('state', models.CharField(choices=[('Success', 'Success'), ('Failed', 'Failed')], default='', max_length=256)),
            ],
        ),
    ]