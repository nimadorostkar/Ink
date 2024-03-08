from django.contrib import admin
from ckeditor.widgets import CKEditorWidget
from blog.models import Post



class PostAdmin(admin.ModelAdmin):
    list_display = ('cover','title','post_date')
    list_filter = ('post_date',)
    search_fields = ('title','body')
admin.site.register(Post, PostAdmin)

