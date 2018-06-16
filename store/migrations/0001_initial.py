# Generated by Django 2.0.2 on 2018-06-16 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
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
        migrations.CreateModel(
            name='Samples',
            fields=[
                ('sample_id', models.AutoField(primary_key=True, serialize=False)),
                ('area_easting', models.IntegerField()),
                ('area_northing', models.IntegerField()),
                ('context_number', models.IntegerField()),
                ('sample_number', models.IntegerField()),
                ('material', models.CharField(max_length=25)),
                ('specific_material', models.CharField(blank=True, max_length=50, null=True)),
                ('exterior_color_hue', models.CharField(blank=True, max_length=6, null=True)),
                ('exterior_color_lightness_value', models.DecimalField(blank=True, decimal_places=2, max_digits=3, null=True)),
                ('exterior_color_chroma', models.IntegerField(blank=True, null=True)),
                ('interior_color_hue', models.CharField(blank=True, max_length=6, null=True)),
                ('interior_color_lightness_value', models.DecimalField(blank=True, decimal_places=2, max_digits=3, null=True)),
                ('interior_color_chroma', models.IntegerField(blank=True, null=True)),
                ('weight_kilograms', models.DecimalField(blank=True, decimal_places=4, max_digits=6, null=True)),
                ('sample_description', models.TextField(blank=True, null=True)),
                ('category', models.CharField(blank=True, max_length=25, null=True)),
                ('subcategory', models.CharField(blank=True, max_length=50, null=True)),
                ('count', models.IntegerField(blank=True, null=True)),
                ('current_location', models.CharField(max_length=50)),
                ('recovery_type', models.CharField(max_length=25)),
                ('problems', models.CharField(blank=True, max_length=300, null=True)),
                ('image_files', models.CharField(blank=True, max_length=50, null=True)),
                ('number_3d_files', models.CharField(blank=True, db_column='3d_files', max_length=50, null=True)),
                ('chronology', models.CharField(blank=True, max_length=100, null=True)),
                ('analysis_request', models.CharField(blank=True, max_length=50, null=True)),
                ('detailed_sample_description', models.TextField(blank=True, null=True)),
                ('bureaucratic_status', models.CharField(blank=True, max_length=25, null=True)),
                ('subjective_significance', models.NullBooleanField()),
                ('museum_inventory_number', models.IntegerField(blank=True, null=True)),
                ('bureaucratic_status_identifier', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'verbose_name_plural': 'samples',
                'db_table': 'samples"."samples',
                'ordering': ['sample_id'],
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Storage',
            fields=[
                ('store_id', models.AutoField(primary_key=True, serialize=False)),
                ('store_name', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('address_1', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('address_2', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('region', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('city', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('zip', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('country', models.CharField(default='Turkey', max_length=200)),
                ('created_by_id', models.CharField(default='user_not_defined', max_length=200)),
                ('created_timestamp', models.DateTimeField(auto_now=True)),
                ('modified_by', models.CharField(default='user_not_defined', max_length=200)),
                ('modified_timestamp', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'stores',
                'db_table': 'samples"."store',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('store_id', models.AutoField(primary_key=True, serialize=False)),
                ('store_name', models.CharField(default='', max_length=200)),
                ('address_1', models.CharField(default='', max_length=200)),
                ('address_2', models.CharField(default='', max_length=200)),
                ('region', models.CharField(default='', max_length=200)),
                ('city', models.CharField(default='', max_length=200)),
                ('zip', models.CharField(default='', max_length=200)),
                ('country', models.CharField(default='Turkey', max_length=200)),
                ('created_timestamp', models.DateTimeField(auto_now_add=True)),
                ('modified_by', models.CharField(default='user_not_defined', max_length=200)),
                ('modified_timestamp', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'stores',
                'db_table': 'samples"."store',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tracking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=255)),
                ('create_date', models.DateTimeField()),
                ('modify_date', models.DateTimeField()),
            ],
        ),
    ]
