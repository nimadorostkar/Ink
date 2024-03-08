from django.db import models
from ckeditor.fields import RichTextField
from django.utils.html import format_html


class Post(models.Model):
    title = models.CharField(max_length=255)
    img = models.ImageField(upload_to='blog')
    body = RichTextField(max_length=10000)
    post_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.title)

    def cover(self):
        return format_html("<img width=40 src='{}'>".format(self.img.url))



