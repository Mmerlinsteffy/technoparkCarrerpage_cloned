from django.contrib import admin
from . models import Job
# Register your models here.
class jobadmin(admin.ModelAdmin):
    list_display=['title','closing_date','company','posted_on']
admin.site.register(Job,jobadmin)