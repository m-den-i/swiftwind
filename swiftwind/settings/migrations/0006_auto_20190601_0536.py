# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-06-01 05:36
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0005_settings_from_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='settings',
            name='additional_currencies',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(choices=[('BYN', 'Belarussian Ruble'), ('EUR', 'Euro'), ('USD', 'US Dollar')], default=[], max_length=3), blank=True, default=[], size=None),
        ),
        migrations.AlterField(
            model_name='settings',
            name='default_currency',
            field=models.CharField(choices=[('BYN', 'Belarussian Ruble'), ('EUR', 'Euro'), ('USD', 'US Dollar')], default='EUR', max_length=3),
        ),
    ]