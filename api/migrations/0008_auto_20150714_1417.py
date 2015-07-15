# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_new_watchers_count'),
    ]

    operations = [
        migrations.RenameField(
            model_name='new',
            old_name='imageUrl',
            new_name='imageURL',
        ),
        migrations.RenameField(
            model_name='new',
            old_name='watchers_count',
            new_name='watch_count',
        ),
    ]
