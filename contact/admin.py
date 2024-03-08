from django.contrib import admin
from contact.models import ContactMessage


class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'create_at', 'status']
    list_filter = ['status']
admin.site.register(ContactMessage, ContactMessageAdmin)