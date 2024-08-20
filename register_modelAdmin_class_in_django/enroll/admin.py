from django.contrib import admin
from enroll.models import student


#Register Model by Decorator
@admin.register(student)

# for show data to table form in admin 
class studentAdmin(admin.ModelAdmin):
    list_display=('id','stuid','stuname','father_name','address','email')
# Register your models here.
# admin.site.register(student,studentAdmin)

'''Register Model byt Decorator:
A decorator can be used to register Modeladmin class
 '''
