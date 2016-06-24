# coding:utf-8
# @author huangpingyi
from django.contrib import admin
from hpy01 import models
# Register your models here.

class CateGroyAdminhpy(admin.ModelAdmin):
    #将类绑定注册到admin里面
    list_display = ('id', 'name')
class ArticleAdminhpy(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'hidden','publish_data')
 #不能显示多对多
admin.site.register(models.Articlehpy,ArticleAdminhpy)
admin.site.register(models.Category,CateGroyAdminhpy)
admin.site.register(models.Commenthpy)
admin.site.register(models.ThumbUp)
admin.site.register(models.UserProfilehpy)
admin.site.register(models.UserGrouphpy)