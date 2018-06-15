# Generated by Django 2.0.2 on 2018-06-15 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_samples'),
    ]

    operations = [
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
            ],
            options={
                'verbose_name_plural': 'stores',
                'db_table': 'samples"."store',
                'managed': False,
            },
        ),
    ]