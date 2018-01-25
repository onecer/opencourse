# coding:utf-8
from __future__ import unicode_literals
from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class UserProfile(AbstractUser):
    nickname = models.CharField(verbose_name=u"用户名", max_length=50)
    birthday = models.DateField(verbose_name=u"生日", null=True, blank=True)
    gender = models.CharField(verbose_name=u"性别", choices=(("male", u'男'), ("female", u'女')),
                              default="female", max_length=6)
    address = models.CharField(verbose_name=u"地址", max_length=100, default=u"")
    mobile = models.CharField(verbose_name=u"手机", max_length=11, null=True, blank=True)
    image = models.ImageField(verbose_name=u"头像", upload_to="images/%Y/%m", default=u"images/default.jpg")

    class Meta:
        verbose_name = u"用户资料"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.username


class VerifyRecord(models.Model):
    verify_code = models.CharField(verbose_name=u"验证码", max_length=20)
    email = models.EmailField(verbose_name=u"邮箱", max_length=50)
    send_type = models.CharField(verbose_name=u"发送类型",
                                 choices=(("register", u"注册"), ("forget", u"忘记密码")), max_length=10)
    send_time = models.DateTimeField(verbose_name=u"发送时间", default=datetime.now)

    class Meta:
        verbose_name = u"邮箱验证码"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return '{0} {1}'.format(self.verify_code, self.email)


class Banner(models.Model):
    title = models.CharField(verbose_name=u"轮播图标题", max_length=50)
    image = models.ImageField(verbose_name=u"图片", upload_to="images/banner/%Y/%m", max_length=100)
    url = models.URLField(verbose_name=u"轮播图地址", max_length=200)
    index = models.IntegerField(verbose_name=u"排序", default=0)
    add_time = models.DateTimeField(verbose_name=u"添加时间", default=datetime.now)

    class Meta:
        verbose_name = u"轮播图"
        verbose_name_plural = verbose_name
