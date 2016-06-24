# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hpy01', '0002_auto_20160604_1338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlehpy',
            name='hidden',
            field=models.BooleanField(default=False, verbose_name='是否隐藏'),
        ),
    ]
