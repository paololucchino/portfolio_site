# Generated by Django 2.0.1 on 2018-01-26 10:21

from django.db import migrations, models
import django.utils.timezone
import projects.models
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('slug', models.SlugField(max_length=250, unique_for_date='start_date')),
                ('body', models.TextField()),
                ('image', models.ImageField(blank=True, upload_to=projects.models.build_timestamped_filename)),
                ('start_date', models.DateField(default=django.utils.timezone.now)),
                ('end_date', models.DateField(blank=True, default=django.utils.timezone.now, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('code_url', models.URLField(blank=True, max_length=250)),
                ('publication_url', models.URLField(blank=True, max_length=250)),
                ('external_url', models.URLField(blank=True, max_length=250)),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default='draft', max_length=10)),
                ('highlight', models.BooleanField(default=False)),
                ('tags', taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
            options={
                'ordering': ('-start_date',),
            },
        ),
    ]
