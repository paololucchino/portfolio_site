# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20180110_1355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='tags',
            field=taggit.managers.TaggableManager(verbose_name='Tags', blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag'),
        ),
    ]
