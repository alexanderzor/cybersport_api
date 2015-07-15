# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_new_imageurl'),
    ]

    operations = [
        migrations.AddField(
            model_name='new',
            name='game',
            field=models.ForeignKey(related_name='news', to='api.Game', null=True),
        ),
    ]
