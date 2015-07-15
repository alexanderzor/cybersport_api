# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_new_game'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='game',
            field=models.ForeignKey(related_name='matches', to='api.Game', null=True),
        ),
        migrations.AddField(
            model_name='stream',
            name='game',
            field=models.ForeignKey(related_name='streams', to='api.Game', null=True),
        ),
        migrations.AddField(
            model_name='video',
            name='game',
            field=models.ForeignKey(related_name='videos', to='api.Game', null=True),
        ),
    ]
