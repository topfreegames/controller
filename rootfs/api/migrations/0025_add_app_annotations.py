# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0024_build_sidecarfile'),
    ]

    operations = [
        migrations.AddField(
            model_name='config',
            name='annotations',
            field=jsonfield.fields.JSONField(blank=True, default={}),
        ),
    ]
