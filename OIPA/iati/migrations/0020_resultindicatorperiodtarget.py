# Generated by Django 2.0.6 on 2018-08-30 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iati', '0019_resultindicatorbaselinedimension'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResultIndicatorPeriodTarget',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.DecimalField(blank=True, decimal_places=10, max_digits=25, null=True)),
            ],
        ),
    ]