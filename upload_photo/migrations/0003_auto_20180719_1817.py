# Generated by Django 2.0.6 on 2018-07-19 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload_photo', '0002_auto_20180719_1745'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attachment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='attachments')),
            ],
        ),
        migrations.RemoveField(
            model_name='document',
            name='upload_by',
        ),
        migrations.RemoveField(
            model_name='mainmodel',
            name='document',
        ),
        migrations.DeleteModel(
            name='Document',
        ),
        migrations.DeleteModel(
            name='MainModel',
        ),
    ]
