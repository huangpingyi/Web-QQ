#
#  @author huangpingyi
#

from django.db import models
from hpy01 import models as hpy_models
# Create your models here.

class QQGrouphpy(models.Model):
    name = models.CharField(max_length=64)
    founder = models.ForeignKey(hpy_models.UserProfilehpy)
    brief = models.TextField(max_length=1024 , default='nothing...')
    admin = models.ManyToManyField(hpy_models.UserProfilehpy, related_name='qq_admimn')
    members = models.ManyToManyField(hpy_models.UserProfilehpy,related_name='qqmembers')
    members_limit = models.IntegerField(default=200)

    def __str__(self):
        return self.name
