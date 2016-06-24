# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hpy01', '0005_auto_20160610_0916'),
    ]

    operations = [
        migrations.AddField(
            model_name='articlehpy',
            name='summary',
            field=models.CharField(default='test', max_length=255),
            preserve_default=False,
        ),
    ]
