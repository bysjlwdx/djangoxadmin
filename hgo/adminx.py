#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from .models import Stu
import xadmin
from xadmin import views
# Register your models here.
# class FelixProjectsAdmin(admin.ModelAdmin):
class BaseSetting(object):
    # 开启主题功能
    enable_themes = True
    use_bootswatch = True
class GlobalSettings(object):
    site_title = u'智轩后台信息管理系统'
    site_footer = u'智轩软件开发'
    menu_style = 'accordion'
xadmin.site.register(views.CommAdminView, GlobalSettings)
class FelixProjectsAdmin(object):
    list_display = ('name', 'gender', 'age', 'address')
    search_fields = ['name', 'gender', 'age', 'address']
    list_filter = ['name', 'gender', 'age', 'address']


xadmin.site.register(Stu, FelixProjectsAdmin)