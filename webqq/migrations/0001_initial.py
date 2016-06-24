# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hpy01', '0008_auto_20160614_1227'),
    ]

    operations = [
        migrations.CreateModel(
            name='QQGrouphpy',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=64)),
                ('brief', models.TextField(max_length=1024, default='nothing')),
                ('members_limit', models.IntegerField(default=200)),
                ('admin', models.ManyToManyField(to='hpy01.UserProfilehpy', related_name='qq_admimn')),
                ('founder', models.ForeignKey(to='hpy01.UserProfilehpy')),
                ('members', models.ManyToManyField(to='hpy01.UserProfilehpy', related_name='qqmembers')),
            ],
        ),
    ]
