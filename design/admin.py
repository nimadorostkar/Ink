from django.contrib import admin
from design.models import Category, Design


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title','img']
admin.site.register(Category, CategoryAdmin)



class DesignAdmin(admin.ModelAdmin):
    list_display = ['img', 'title', 'category', 'portfolio_homepage']
    list_filter = ('portfolio_homepage', 'category')
    search_fields = ('title', 'description')
admin.site.register(Design, DesignAdmin)