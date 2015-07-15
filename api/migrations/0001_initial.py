# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('image', models.ImageField(upload_to=b'')),
            ],
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('competitor1ImageUrl', models.URLField()),
                ('competitor2ImageUrl', models.URLField()),
                ('startDate', models.DateTimeField()),
                ('endDate', models.DateTimeField()),
                ('gameUrl', models.URLField()),
                ('score1', models.IntegerField()),
                ('score2', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='New',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=300)),
                ('date', models.DateField(auto_now_add=True)),
                ('description', models.TextField()),
                ('source', models.URLField(blank=True)),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
        migrations.CreateModel(
            name='Stream',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('imageUrl', models.URLField()),
                ('channel', models.CharField(max_length=200)),
                ('watchers_count', models.IntegerField()),
                ('url_high', models.URLField()),
                ('url_low', models.URLField()),
                ('url_sound', models.URLField()),
                ('videoType', models.IntegerField()),
                ('duration', models.DurationField()),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('watchCount', models.IntegerField()),
                ('duration', models.DurationField()),
                ('date', models.DateTimeField()),
                ('videoUrl', models.URLField()),
            ],
        ),
    ]
