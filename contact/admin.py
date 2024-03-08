from django.contrib import admin
from contact.models import ContactMessage


class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'create_at', 'status']
    list_filter = ('create_at','update_at','status')
    search_fields = ('name', 'message','email')
admin.site.register(ContactMessage, ContactMessageAdmin)