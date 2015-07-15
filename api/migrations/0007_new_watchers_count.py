# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_game_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='new',
            name='watchers_count',
            field=models.IntegerField(null=True),
        ),
    ]
