from django.contrib import admin
from homepage.models import HomepageInfo

class HomepageInfoAdmin(admin.ModelAdmin):
    list_display = ('name','short_description')
admin.site.register(HomepageInfo, HomepageInfoAdmin)





admin.site.site_header = "Admin Panel"
admin.site.site_title = "Admin Panel"
admin.site.index_title = "Welcome to your portal"