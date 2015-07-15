# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20150713_1209'),
    ]

    operations = [
        migrations.AddField(
            model_name='new',
            name='imageUrl',
            field=models.URLField(null=True),
        ),
    ]
