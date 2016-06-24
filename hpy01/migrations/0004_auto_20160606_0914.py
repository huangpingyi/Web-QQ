# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hpy01', '0003_auto_20160605_0245'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Categoryhpy',
            new_name='Category',
        ),
        migrations.AlterField(
            model_name='articlehpy',
            name='author',
            field=models.OneToOneField(to='hpy01.UserProfilehpy', verbose_name='作者'),
        ),
        migrations.AlterField(
            model_name='articlehpy',
            name='publish_data',
            field=models.DateTimeField(auto_now=True, verbose_name='发布时间'),
        ),
    ]
