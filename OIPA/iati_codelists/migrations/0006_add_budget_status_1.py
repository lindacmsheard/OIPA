# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-08 15:54
from __future__ import unicode_literals

from django.db import migrations, models
from django.contrib.contenttypes.management import update_contenttypes
import django.db.models.deletion


def add_budget_status(apps, schema_editor):
    """
    add budget status 1 as its used as default in iati migration 0036
    """
    update_contenttypes(apps.get_app_config('iati'), interactive=False) # make sure all content types exist

    try: # don't run on first migration
        BudgetStatus = apps.get_model('iati_codelists', 'BudgetStatus')
    except:
        return

    if not BudgetStatus.objects.filter(code='1').exists(): 
        BudgetStatus(
            code='1', 
            name='Indicative', 
            description='A non-binding estimate for the described budget.').save()


class Migration(migrations.Migration):

    dependencies = [
        ('iati_codelists', '0005_auto_20160602_1644'),
        ('contenttypes', '0002_remove_content_type_name'),
        ('iati', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_budget_status),
    ]
