# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Articlehpy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('title', models.CharField(max_length=255, unique=True, verbose_name='文章标题')),
                ('head_img', models.ImageField(upload_to='uploads')),
                ('content', models.TextField(verbose_name='内容')),
                ('publish_data', models.DateTimeField(auto_now=True)),
                ('hidden', models.BooleanField(default=True)),
                ('priority', models.IntegerField(default=1000, verbose_name='优先级')),
            ],
        ),
        migrations.CreateModel(
            name='Categoryhpy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=64, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Commenthpy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('comment', models.TextField(max_length=1000)),
                ('date', models.DateTimeField(auto_now=True)),
                ('article', models.ForeignKey(to='hpy01.Articlehpy')),
                ('parent_comment', models.ForeignKey(related_name='p_comment', to='hpy01.Commenthpy')),
            ],
        ),
        migrations.CreateModel(
            name='ThumUp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('date', models.DateTimeField(auto_now=True)),
                ('article', models.ForeignKey(to='hpy01.Articlehpy')),
            ],
        ),
        migrations.CreateModel(
            name='UserGrouphpy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=64, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfilehpy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=32)),
                ('groups', models.ManyToManyField(to='hpy01.UserGrouphpy')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='thumup',
            name='user',
            field=models.ForeignKey(to='hpy01.UserProfilehpy'),
        ),
        migrations.AddField(
            model_name='commenthpy',
            name='user',
            field=models.ForeignKey(to='hpy01.UserProfilehpy'),
        ),
        migrations.AddField(
            model_name='categoryhpy',
            name='admin',
            field=models.ForeignKey(to='hpy01.UserProfilehpy'),
        ),
        migrations.AddField(
            model_name='articlehpy',
            name='author',
            field=models.OneToOneField(to='hpy01.UserProfilehpy'),
        ),
        migrations.AddField(
            model_name='articlehpy',
            name='category',
            field=models.ForeignKey(verbose_name='板块', to='hpy01.Categoryhpy'),
        ),
    ]
