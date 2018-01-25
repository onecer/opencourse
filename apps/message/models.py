# coding:utf-8
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class UserMessage(models.Model):
    name = models.CharField(verbose_name=u"名字", max_length=50)
    email = models.EmailField(verbose_name=u"邮箱地址")
    address = models.CharField(verbose_name=u"联系地址", max_length=100)
    message = models.CharField(verbose_name=u"留言", max_length=100)

    class Meta:
        verbose_name = u'用户记录'
        verbose_name_plural = verbose_name
