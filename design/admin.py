from django.contrib import admin
from design.models import Category, Design


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title',]
admin.site.register(Category, CategoryAdmin)



class DesignAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'portfolio_homepage']
    list_filter = ['portfolio_homepage',]
admin.site.register(Design, DesignAdmin)