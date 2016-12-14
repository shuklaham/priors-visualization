from django.contrib import admin

# Register your models here.
from models import Report

class ReportAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ['name']


admin.site.register(Report,ReportAdmin)