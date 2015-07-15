# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='competitor1',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='match',
            name='competitor2',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
