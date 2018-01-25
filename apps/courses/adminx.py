# _*_ coding:utf-8 _*_
# Author: Onecer <LDH@QQ.COM>
# Date: 1/21/18 2:36 AM
import xadmin

from .models import Course, Lesson, Video, CourseResource


class CourseAdmin(object):
    list_display = ['title', 'level', 'students', 'lesson_chapters', 'lesson_type', 'image', 'fav_nums', 'click_nums',
                    'add_time']
    list_filter = ['title', 'level', 'students', 'lesson_chapters', 'lesson_type', 'fav_nums', 'click_nums', 'add_time']
    search_fields = ['title', 'level', 'students', 'lesson_chapters', 'lesson_type']


class LessonAdmin(object):
    list_display = ['course', 'name', 'add_time']
    list_filter = ['course__title', 'name', 'add_time']
    search_fields = ['course', 'name']


class VideoAdmin(object):
    list_display = ['lesson', 'name', 'add_time']
    list_filter = ['lesson__name', 'name', 'add_time']
    search_fields = ['lesson', 'name']


class CourseResourceAdmin(object):
    list_display = ['course', 'name', 'download', 'add_time']
    list_filter = ['course__title', 'name', 'add_time']
    search_fields = ['course', 'name']


xadmin.site.register(Course, CourseAdmin)
xadmin.site.register(Lesson, LessonAdmin)
xadmin.site.register(Video, VideoAdmin)
xadmin.site.register(CourseResource, CourseResourceAdmin)
