# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='code_url',
            field=models.URLField(max_length=250, blank=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='end_date',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='project',
            name='external_url',
            field=models.URLField(max_length=250, blank=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='image_url',
            field=models.CharField(max_length=250, blank=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='publication_url',
            field=models.URLField(max_length=250, blank=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='slug',
            field=models.SlugField(max_length=250, unique_for_date='start_date'),
        ),
    ]
