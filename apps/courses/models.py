# coding:utf-8
from __future__ import unicode_literals
from datetime import datetime

from django.db import models

# Create your models here.


class Course(models.Model):
    title = models.CharField(verbose_name=u"课程标题", max_length=100)
    desc = models.CharField(verbose_name=u"课程简介", max_length=300)
    level = models.CharField(verbose_name=u"难度等级",
                             choices=(("cj", u"初级"), ("zj", u"中级"), ("gj", u"高级")), max_length=5)
    students = models.IntegerField(verbose_name=u"学习人数", default=0)
    lesson_times = models.IntegerField(verbose_name=u"课程时间(分钟)", default=0)
    lesson_chapters = models.IntegerField(verbose_name=u"课程章节", default=0)
    lesson_type = models.CharField(verbose_name=u"课程类别", max_length=50)
    fav_nums = models.IntegerField(verbose_name=u"收藏人数", default=0)
    click_nums = models.IntegerField(verbose_name=u"点击人数", default=0)
    image = models.ImageField(verbose_name=u"封面图片", upload_to="images/courses/%Y/%m", max_length=100)
    detail = models.TextField(verbose_name=u"课程详情")
    add_time = models.DateTimeField(verbose_name=u"添加时间", default=datetime.now)

    class Meta:
        verbose_name = u"课程"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.title


class Lesson(models.Model):
    course = models.ForeignKey(Course, verbose_name=u"课程")
    name = models.CharField(verbose_name=u"视频名", max_length=100)
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"章节"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


class Video(models.Model):
    lesson = models.ForeignKey(Lesson, verbose_name=u"课程名")
    name = models.CharField(verbose_name=u"视频名", max_length=100)
    add_time = models.DateTimeField(verbose_name=u"添加时间", default=datetime.now)

    class Meta:
        verbose_name = u"视频"
        verbose_name_plural = verbose_name


class CourseResource(models.Model):
    course = models.ForeignKey(Course, verbose_name=u"课程")
    name = models.CharField(verbose_name=u"名称", max_length=100)
    download = models.FileField(upload_to="courses/resource/%Y/%m", verbose_name=u"课程资源", max_length=100)
    add_time = models.DateTimeField(verbose_name=u"添加时间", default=datetime.now)

    class Meta:
        verbose_name = u"课程资源"
        verbose_name_plural = verbose_name
