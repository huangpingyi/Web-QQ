# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hpy01', '0007_auto_20160614_0138'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofilehpy',
            name='friends',
            field=models.ManyToManyField(to='hpy01.UserProfilehpy', related_name='friends_rel_+', blank=True),
        ),
        migrations.AlterField(
            model_name='articlehpy',
            name='author',
            field=models.ForeignKey(to='hpy01.UserProfilehpy', verbose_name='作者'),
        ),
    ]
