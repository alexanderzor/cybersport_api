# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_video_videotype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='endDate',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='match',
            name='gameUrl',
            field=models.URLField(null=True),
        ),
        migrations.AlterField(
            model_name='match',
            name='startDate',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='video',
            name='duration',
            field=models.DurationField(null=True),
        ),
        migrations.AlterField(
            model_name='video',
            name='watchCount',
            field=models.IntegerField(null=True),
        ),
    ]
