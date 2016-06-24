# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hpy01', '0006_articlehpy_summary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlehpy',
            name='author',
            field=models.ForeignKey(unique=True, to='hpy01.UserProfilehpy', verbose_name='作者'),
        ),
    ]
