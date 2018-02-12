from django.contrib import admin
from .models import C_plus,BinaryTree,Student
# Register your models here.

class CPlusAdmin(admin.ModelAdmin):
	list_display = ('topic','text')
admin.site.register(C_plus,CPlusAdmin)

class BinaryTreeAdmin(admin.ModelAdmin):
	list_display = ('question','answer')
admin.site.register(BinaryTree,BinaryTreeAdmin)


class StudentAdmin(admin.ModelAdmin):
	list_display = ('faculty_no','branch','cpi')
admin.site.register(Student,StudentAdmin) 
#	list_display = ('faculty_no','branch','cpi')
#admin.site.register(Student,StudentAdmin) 