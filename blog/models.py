from django.db import models
from ckeditor.fields import RichTextField


class Post(models.Model):
    title = models.CharField(max_length=255)
    img = models.ImageField(upload_to='blog',null=True,blank=True)
    body = RichTextField(max_length=1000)
    post_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.title)



