# Generated by Django 2.0.6 on 2018-07-16 09:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('botany', '0003_auto_20180712_2306'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='botany',
            options={'managed': False, 'verbose_name_plural': 'Botany'},
        ),
        migrations.AlterModelOptions(
            name='fraction',
            options={'managed': False, 'verbose_name_plural': 'Fraction'},
        ),
        migrations.AlterModelOptions(
            name='fractioncomposition',
            options={'managed': False, 'verbose_name_plural': 'Composition'},
        ),
        migrations.AlterModelOptions(
            name='fractionmaterialspresent',
            options={'managed': False, 'verbose_name_plural': 'Materials Present'},
        ),
    ]