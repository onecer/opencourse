# _*_ coding:utf-8 _*_
# Author: Onecer <LDH@QQ.COM>
# Date: 1/21/18 3:05 AM
import xadmin

from .models import CityDict, CourseOrg, Teacher


class CityDictAdmin(object):
    list_display = ['name', 'desc', 'add_time']
    list_filter = ['name', 'add_time']
    search_fields = ['name']


class CourseOrgAdmin(object):
    list_display = ['name', 'desc', 'click_nums', 'fav_nums', 'address', 'city', 'add_time', 'image']
    list_filter = ['name', 'click_nums', 'fav_nums', 'address', 'city', 'add_time']
    search_fields = ['name', 'desc']


class TeacherAdmin(object):
    list_display = ['org', 'name', 'work_years', 'work_company', 'work_position', 'click_nums', 'fav_nums', 'add_time']
    list_filter = ['org__name', 'name', 'work_years', 'work_company', 'work_position', 'click_nums', 'fav_nums', 'add_time']
    search_fields = ['org', 'name']


xadmin.site.register(CityDict, CityDictAdmin)
xadmin.site.register(Teacher, TeacherAdmin)
xadmin.site.register(CourseOrg, CourseOrgAdmin)