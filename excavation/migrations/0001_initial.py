# Generated by Django 2.0.6 on 2018-06-27 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Context',
            fields=[
                ('context_id', models.AutoField(primary_key=True, serialize=False)),
                ('area_easting', models.IntegerField(null=True)),
                ('area_northing', models.IntegerField(null=True)),
                ('context_number', models.IntegerField(null=True)),
                ('context_type', models.CharField(blank=True, max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('deposition_interpretation', models.CharField(blank=True, max_length=500, null=True)),
                ('subtable', models.CharField(blank=True, max_length=25, null=True)),
                ('chronology', models.CharField(blank=True, max_length=100, null=True)),
                ('chronology_source', models.CharField(blank=True, max_length=100, null=True)),
                ('stratigraphic_narrative', models.CharField(blank=True, max_length=500, null=True)),
            ],
            options={
                'db_table': 'excavation"."contexts',
                'managed': False,
            },
        ),
    ]
