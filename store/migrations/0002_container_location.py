# Generated by Django 2.0.2 on 2018-06-15 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Container',
            fields=[
                ('container_id', models.AutoField(primary_key=True, serialize=False)),
                ('container_name', models.CharField(blank=True, max_length=50, null=True)),
                ('container_type', models.CharField(blank=True, max_length=50, null=True)),
                ('sample_id', models.IntegerField(blank=True, null=True)),
                ('current_location_tmp', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'verbose_name_plural': 'containers',
                'db_table': 'samples"."container',
                'ordering': ['container_name'],
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('location_id', models.AutoField(primary_key=True, serialize=False)),
                ('location_identifier', models.IntegerField(blank=True, null=True)),
                ('location_type', models.CharField(blank=True, max_length=100, null=True)),
                ('current_location_tmp', models.CharField(blank=True, max_length=100, null=True)),
                ('location_name', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'verbose_name_plural': 'locations',
                'db_table': 'samples"."location',
                'ordering': ['location_name'],
                'managed': False,
            },
        ),
    ]