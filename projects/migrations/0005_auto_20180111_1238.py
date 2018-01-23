# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_auto_20180110_1400'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='image_url',
        ),
        migrations.AddField(
            model_name='project',
            name='image',
            field=models.ImageField(blank=True, upload_to='projects'),
        ),
    ]
