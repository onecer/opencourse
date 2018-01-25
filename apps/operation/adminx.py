# _*_ coding:utf-8 _*_
# Author: Onecer <LDH@QQ.COM>
# Date: 1/21/18 3:17 AM
import xadmin

from .models import UserMessage, UserAsk, UserCourse, UserFavorite, CourseCommets


class UserMessageAdmin(object):
    list_display = ['user', 'message', 'has_read', 'add_time']
    list_filter = ['user', 'message', 'has_read', 'add_time']
    search_fields = ['user', 'message']


class UserAskAdmin(object):
    list_display = ['name', 'mobile', 'course_name', 'add_time']
    list_filter = ['name', 'mobile', 'course_name', 'add_time']
    search_fields = ['name', 'mobile', 'course_name']


class UserFavoriteAdmin(object):
    list_display = ['user', 'course', 'fav_id', 'fav_type', 'add_time']
    list_filter = ['user', 'course', 'fav_id', 'fav_type', 'add_time']
    search_fields = ['user', 'course']


class CourseCommetsAdmin(object):
    list_display = ['user', 'course', 'comment', 'add_time']
    list_filter = ['user', 'course', 'comment', 'add_time']
    search_fields = ['user', 'course', 'comment']


class UserCourseAdmin(object):
    list_display = ['user', 'course', 'add_time']
    list_filter = ['user', 'course', 'add_time']
    search_fields = ['user', 'course']


xadmin.site.register(UserFavorite, UserFavoriteAdmin)
xadmin.site.register(UserCourse, UserCourseAdmin)
xadmin.site.register(UserAsk, UserAskAdmin)
xadmin.site.register(UserMessage, UserMessageAdmin)
xadmin.site.register(CourseCommets, CourseCommetsAdmin)
