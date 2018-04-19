# Generated by Django 2.0.4 on 2018-04-11 00:02

import ckeditor.fields
from django.db import migrations, models
import django.utils.timezone
import stdimage.models
import stdimage.utils


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='New',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80)),
                ('content', ckeditor.fields.RichTextField()),
                ('slug', models.SlugField()),
                ('image', stdimage.models.StdImageField(blank=True, upload_to=stdimage.utils.UploadToUUID(path=''))),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published', models.BooleanField(default=True)),
            ],
        ),
    ]
