# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-22 16:50
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iati', '0049_planned_disbursement_period_end_null'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='point_pos',
            field=django.contrib.gis.db.models.fields.PointField(default=None, geography=True, null=True, srid=4326),
        ),
    ]