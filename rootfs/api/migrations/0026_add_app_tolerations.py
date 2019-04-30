# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0025_add_app_annotations'),
    ]

    operations = [
        migrations.AddField(
            model_name='config',
            name='tolerations',
            field=jsonfield.fields.JSONField(blank=True, default={}),
        ),
    ]
