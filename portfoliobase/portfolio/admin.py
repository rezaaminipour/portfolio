from django.contrib import admin
from .models import SiteSetting, SocialLink, EmploymentHistory

@admin.register(SiteSetting)
class SiteSettingAdmin(admin.ModelAdmin):
    list_display = ['site_name']

@admin.register(SocialLink)
class SocialLinkAdmin(admin.ModelAdmin):
    list_display = ['platform', 'username', 'is_active', 'order']
    list_editable = ['is_active', 'order']

@admin.register(EmploymentHistory)
class EmploymentHistoryAdmin(admin.ModelAdmin):
    list_display = ['job_title', 'company', 'start_date', 'end_date', 'is_current', 'order']
    list_editable = ['order']
