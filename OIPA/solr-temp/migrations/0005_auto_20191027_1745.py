# Generated by Django 2.0.13 on 2019-10-27 17:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('solr', '0004_udpated_fields_name_transaction_id_and_result_id'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ActivityDelete',
        ),
        migrations.DeleteModel(
            name='DatasetNoteDelete',
        ),
        migrations.DeleteModel(
            name='ResultDelete',
        ),
        migrations.DeleteModel(
            name='TransactionDelete',
        ),
    ]
