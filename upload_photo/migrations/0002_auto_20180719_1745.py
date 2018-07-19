# Generated by Django 2.0.6 on 2018-07-19 14:45

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('upload_photo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datestamp', models.DateTimeField(auto_now_add=True)),
                ('document', models.FileField(upload_to='uploads/')),
                ('upload_by', models.ForeignKey(on_delete='PROTECT', related_name='uploaded_documents', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MainModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=42)),
                ('document', models.ForeignKey(on_delete='PROTECT', to='upload_photo.Document')),
            ],
        ),
        migrations.DeleteModel(
            name='Photo',
        ),
    ]
