# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hpy01', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commenthpy',
            name='parent_comment',
            field=models.ForeignKey(blank=True, null=True, related_name='p_comment', to='hpy01.Commenthpy'),
        ),
    ]
