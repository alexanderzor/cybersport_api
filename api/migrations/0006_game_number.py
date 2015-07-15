# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20150713_1528'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='number',
            field=models.IntegerField(default=3),
            preserve_default=False,
        ),
    ]
