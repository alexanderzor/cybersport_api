# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_auto_20150714_1417'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='videoType',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
    ]
