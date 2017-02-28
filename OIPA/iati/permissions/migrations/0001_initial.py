# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-28 16:25
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('iati_synchroniser', '0001_initial'),
        ('auth', '0008_alter_user_username_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='OrganisationAdminGroup',
            fields=[
                ('group_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='auth.Group')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name_plural': 'Organisation admin groups',
            },
            bases=('auth.group',),
        ),
        migrations.CreateModel(
            name='OrganisationGroup',
            fields=[
                ('group_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='auth.Group')),
                ('publisher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='iati_synchroniser.Publisher', unique=True)),
            ],
            options={
                'ordering': ['name'],
                'verbose_name_plural': 'Organisation groups',
            },
            bases=('auth.group',),
        ),
        migrations.CreateModel(
            name='OrganisationUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('iati_api_key', models.CharField(blank=True, max_length=255, null=True)),
                ('iati_user_id', models.CharField(blank=True, max_length=255, null=True)),
                ('organisation_admin_groups', models.ManyToManyField(blank=True, related_name='organisationuser_set', to='permissions.OrganisationAdminGroup', verbose_name=b'Organisation Admin Groups')),
                ('organisation_groups', models.ManyToManyField(blank=True, related_name='organisationuser_set', to='permissions.OrganisationGroup', verbose_name=b'Organisation Groups')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='organisationuser', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Organisation users',
            },
        ),
        migrations.AddField(
            model_name='organisationadmingroup',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='permissions.OrganisationUser'),
        ),
        migrations.AddField(
            model_name='organisationadmingroup',
            name='publisher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='iati_synchroniser.Publisher', unique=True),
        ),
    ]
