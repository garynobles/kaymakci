# Generated by Django 2.0.6 on 2018-07-02 19:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spatial3d', '0002_auto_20180702_2144'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='photobatch',
            options={'managed': False, 'ordering': ['-folder_processed', 'photobatch_id']},
        ),
        migrations.AlterModelTable(
            name='photobatch',
            table='excavation"."photobatch_processing',
        ),
    ]