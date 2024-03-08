from django.contrib import admin
from homepage.models import HomepageInfo

class HomepageInfoAdmin(admin.ModelAdmin):
    list_display = ('name','short_description')
admin.site.register(HomepageInfo, HomepageInfoAdmin)

