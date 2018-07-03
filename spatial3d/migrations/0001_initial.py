# Generated by Django 2.0.6 on 2018-07-02 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Photobatch',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('photobatch_id', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('prefix', models.CharField(blank=True, max_length=200, null=True)),
                ('area_easting', models.IntegerField(choices=[('', ''), (99, 99), (108, 108), (109, 109)])),
                ('area_northing', models.IntegerField(choices=[('', ''), (523, 523), (526, 526), (3, 1)])),
                ('context_number', models.IntegerField()),
                ('number_of_photos', models.IntegerField(blank=True, null=True)),
                ('number_targets', models.IntegerField(blank=True, null=True)),
                ('processed_on', models.CharField(blank=True, choices=[('', ''), ('Cyrus', 'Cyrus'), ('Harpagus', 'Harpagus'), ('Pissuthnes', 'Pissuthnes'), ('Struthas', 'Struthas'), ('Tissaphernes', 'Tissaphernes')], default='', max_length=200, null=True)),
                ('processed_by', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('camera_model', models.CharField(blank=True, default='samsung', max_length=200, null=True)),
                ('imported_photoscan', models.NullBooleanField()),
                ('aligned', models.NullBooleanField(choices=[('', ''), (True, 'Yes'), (False, 'No')])),
                ('align_accuracy', models.CharField(default='medium', max_length=200)),
                ('align_pair_selection', models.CharField(default='disabled', max_length=200)),
                ('align_keypoint_limit', models.IntegerField(default=40000)),
                ('align_tiepoint_limit', models.IntegerField(default=4000)),
                ('detected_targets', models.NullBooleanField(choices=[('', ''), (True, 'Yes'), (False, 'No')])),
                ('target_type', models.CharField(default='circular 12 bit', max_length=200)),
                ('target_tolerance', models.IntegerField(default=50)),
                ('target_origional_error', models.IntegerField(blank=True, null=True)),
                ('target_optimised_error', models.IntegerField(blank=True, null=True)),
                ('dense_pointcloud', models.NullBooleanField(choices=[('', ''), (True, 'Yes'), (False, 'No')])),
                ('mesh', models.NullBooleanField(choices=[('', ''), (True, 'Yes'), (False, 'No')])),
                ('mesh_type', models.CharField(default='arbitrary', max_length=200)),
                ('mesh_face_count', models.CharField(default='medium', max_length=200)),
                ('mesh_interpolation', models.CharField(default='disabled', max_length=200)),
                ('texture', models.NullBooleanField(choices=[('', ''), (True, 'Yes'), (False, 'No')])),
                ('texture_defaults', models.IntegerField(blank=True, default=8500, null=True)),
                ('dem', models.NullBooleanField(choices=[('', ''), (True, 'Yes'), (False, 'No')])),
                ('dem_coordinate_system', models.IntegerField(default=32635)),
                ('dem_source_data', models.CharField(default='dense cloud', max_length=200)),
                ('dem_interpolation', models.CharField(default='disabled', max_length=200)),
                ('orthomosaic', models.NullBooleanField(choices=[('', ''), (True, 'Yes'), (False, 'No')])),
                ('orthomosaic_type', models.CharField(default='geographic', max_length=200)),
                ('orthomosaic_pixel_size', models.DecimalField(blank=True, decimal_places=6, default=0.005, max_digits=10, null=True)),
                ('export_points', models.NullBooleanField(choices=[('', ''), (True, 'Yes'), (False, 'No')])),
                ('export_points_filename', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('export_points_offsets', models.CharField(default='X=580000 Y=4275000 Z=0', max_length=200)),
                ('export_report_pdf', models.NullBooleanField(choices=[('', ''), (True, 'Yes'), (False, 'No')])),
                ('export_orthophoto', models.NullBooleanField(choices=[('', ''), (True, 'Yes'), (False, 'No')])),
                ('export_dem', models.NullBooleanField(choices=[('', ''), (True, 'Yes'), (False, 'No')])),
                ('export_dem_pixel_size', models.DecimalField(blank=True, decimal_places=6, default=0.005, max_digits=10, null=True)),
                ('export_dem_geodatabase', models.NullBooleanField(choices=[('', ''), (True, 'Yes'), (False, 'No')])),
                ('folder_processed', models.NullBooleanField(choices=[('', ''), (True, 'Yes'), (False, 'No')])),
                ('processing_notes', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/notes/')),
                ('created_timestamp', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.CharField(default='user_not_defined', max_length=200)),
            ],
            options={
                'db_table': 'excavation"."photobatch_processing',
                'ordering': ['-created_timestamp'],
                'managed': False,
            },
        ),
    ]
