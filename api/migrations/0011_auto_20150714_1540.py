# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_auto_20150714_1539'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='gameUrl',
            field=models.URLField(null=True, blank=True),
        ),
    ]
