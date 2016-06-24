#!/usr/bin/python
# coding:utf8
#author huangpingyi

from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Articlehpy(models.Model):
    #帖子表
    title = models.CharField(u"文章标题", max_length=255, unique=True)
    #标题长度，不能重名
    category = models.ForeignKey("Category", verbose_name="板块")
    #发布版块，外键关联Categoryhpy加引号表示已反射形式添加。Catagoryhpy在Articlehpy雷后面x
    head_img =models.ImageField(upload_to="uploads")
    #在当前目录子目录
    summary = models.CharField(max_length=255)
    content = models.TextField(u"内容")
    #用TextField不用CharField文章可能过长。
    author = models.ForeignKey('UserProfilehpy',verbose_name='作者')
    #userprofilehpy = models.ForeignKey('UserProfilehpy')
    publish_data = models.DateTimeField(auto_now= True,verbose_name='发布时间')
    #时间不用自己写
    hidden = models.BooleanField(default=False,verbose_name="是否隐藏")
    #帖子是给别人看，还是只能自己
    priority = models.IntegerField(u"优先级",default=1000)
    #帖子顺序有些制定


    def __str__(self):
        return "<%s,author:%s>" % (self.title, self.author)

class Commenthpy(models.Model):
    #评论表
    article = models.ForeignKey("Articlehpy")
    #评论文章
    user = models.ForeignKey('UserProfilehpy')
     #评论下面可以还有多个评论，sql不能自关联。python提供，有多层。父字段，自己。
    # parent_comment = models.ForeignKey('Commenthpy',)
    parent_comment = models.ForeignKey('self', related_name='p_comment', blank=True, null=True)
    #blank admin ,null数据库
    comment = models.TextField(max_length=1000)
    date = models.DateTimeField(auto_now=True)
    def __str__(self):
        return "<user:%s>" % ( self.user)
class ThumbUp(models.Model):
    #点赞
    article = models.ForeignKey('Articlehpy')
    user = models.ForeignKey('UserProfilehpy')
    date = models.DateTimeField(auto_now=True)
    def __str__(self):
        return u"<user:%s>" % (self.user,)
class Category(models.Model):
    #板块表
    name =models.CharField(max_length=64, unique=True)
    admin =models.ForeignKey('UserProfilehpy')
    def __str__(self):
        return self.name
class UserProfilehpy(models.Model):
    #账户信息
    user = models.OneToOneField(User)
    #用django自带的认账系统,限制一个账户关联一个
   # id = models.IntegerField(id(user))
    name = models.CharField(max_length=32)
    groups = models.ManyToManyField('UserGrouphpy')
    friends = models.ManyToManyField('self', blank=True,related_name='my_friends')
    #blank对称关系，微博非对称symmetrical

    def __str__(self):
        return self.name
class UserGrouphpy(models.Model):
    #角色表
    name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.name