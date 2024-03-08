from django.db import models
from django.utils.html import format_html


class Category(models.Model):
    title = models.CharField(max_length=100,blank=True,null=True)
    description = models.TextField(max_length=1000,blank=True,null=True)
    image = models.ImageField(upload_to='cat',default="cat/default.png")

    def __str__(self):
        return self.title



class Design(models.Model):
    title = models.CharField(max_length=200,null=True,blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    description = models.TextField(max_length=1000,null=True,blank=True)
    image = models.ImageField(upload_to='designs')
    portfolio_homepage = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def img(self):
        return format_html("<img width=40 src='{}'>".format(self.image.url))


