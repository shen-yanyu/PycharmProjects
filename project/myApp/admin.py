from django.contrib import admin

# Register your models here.
# #
from .models import Grades, Students
#
# # 注册
#class GradesAdmin(admin.ModelAdmin):
# #
# # 列表页属性
#    list_display = ['pk', 'gname', 'gdate', 'ggrilnum', 'gboynum', 'isDelete']
#     list_filter = ['gname']
#     search_fields = ['gname']
#     list_per_page = [5]
#
# #     添加，修改页属性
#     fields = ['ggirlnum', 'gboynum', 'gname', 'gdate', 'isDelete']
#     fieldsets = [ ("num",{"fields":['ggirlnum', 'gboynum']}),
#                  ("base", {"fields":["gname", "gdate", "isDelete"]}),]
#
#


admin.site.register(Grades)
admin.site.register(Students)
