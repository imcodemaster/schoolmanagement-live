from django.contrib import admin
from .models import Teacher, Notice
from django.contrib.admin.options import ModelAdmin


# Register your models here.
class TeacherAdmin(ModelAdmin):
	list_display = ['name', 'qualification', 'phonenumber']
	search_field = ['name']
	list_filter = ['salary', 'qualification']

admin.site.register(Teacher, TeacherAdmin)

class NoticeAdmin(ModelAdmin):
	list_display = ['title', 'author','published']
	search_field = ['name', 'author', 'published']
	list_filter = ['title', 'published']

admin.site.register(Notice, NoticeAdmin)
