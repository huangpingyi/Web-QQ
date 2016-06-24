# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hpy01', '0004_auto_20160606_0914'),
    ]

    operations = [
        migrations.CreateModel(
            name='ThumbUp',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now=True)),
                ('article', models.ForeignKey(to='hpy01.Articlehpy')),
                ('user', models.ForeignKey(to='hpy01.UserProfilehpy')),
            ],
        ),
        migrations.RemoveField(
            model_name='thumup',
            name='article',
        ),
        migrations.RemoveField(
            model_name='thumup',
            name='user',
        ),
        migrations.DeleteModel(
            name='ThumUp',
        ),
    ]
