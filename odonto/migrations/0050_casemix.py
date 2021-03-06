# Generated by Django 2.0.13 on 2020-10-14 15:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import opal.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('opal', '0038_auto_20191206_1449'),
        ('odonto', '0049_auto_20200702_1558'),
    ]

    operations = [
        migrations.CreateModel(
            name='CaseMix',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(blank=True, null=True)),
                ('updated', models.DateTimeField(blank=True, null=True)),
                ('consistency_token', models.CharField(max_length=8)),
                ('ability_to_communicate', models.CharField(choices=[('0', '0'), ('A', 'A'), ('B', 'B'), ('C', 'C')], max_length=256, null=True)),
                ('ability_to_cooperate', models.CharField(choices=[('0', '0'), ('A', 'A'), ('B', 'B'), ('C', 'C')], max_length=256, null=True, verbose_name='Ability To Co-operate')),
                ('medical_status', models.CharField(choices=[('0', '0'), ('A', 'A'), ('B', 'B'), ('C', 'C')], max_length=256, null=True)),
                ('oral_risk_factors', models.CharField(choices=[('0', '0'), ('A', 'A'), ('B', 'B'), ('C', 'C')], max_length=256, null=True)),
                ('access_to_oral_care', models.CharField(choices=[('0', '0'), ('A', 'A'), ('B', 'B'), ('C', 'C')], max_length=256, null=True)),
                ('legal_and_ethical_barriers_to_care', models.CharField(choices=[('0', '0'), ('A', 'A'), ('B', 'B'), ('C', 'C')], max_length=256, null=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_odonto_casemix_subrecords', to=settings.AUTH_USER_MODEL)),
                ('episode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='opal.Episode')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_odonto_casemix_subrecords', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=(opal.models.UpdatesFromDictMixin, opal.models.ToDictMixin, models.Model),
        ),
    ]
