# _*_ coding:utf-8 _*_
import xadmin
from xadmin import views

from .models import VerifyRecord, Banner


class BaseSettings(object):
    enable_themes = True
    use_bootswatch = True

class GlobalSettings(object):
    site_title = '开源课程网'
    site_footer = '开源课程网'
    menu_style = 'accordion'  # 设置菜单可收缩,手风琴 accordion


class VerifyRecordAdmin(object):
    list_display = ["verify_code", "email", "send_type", "send_time"]
    list_filter = ["verify_code", "email", "send_type", "send_time"]
    search_fields = ["verify_code", "email"]


class BannerAdmin(object):
    list_display = ["title", "image", "url", "index", "add_time"]
    list_filter = ["title", "image", "url", "index", "add_time"]
    search_fields = ["title", "image", "url", "index"]


xadmin.site.register(Banner, BannerAdmin)
xadmin.site.register(VerifyRecord, VerifyRecordAdmin)
xadmin.site.register(views.BaseAdminView, BaseSettings)
xadmin.site.register(views.CommAdminView, GlobalSettings)
