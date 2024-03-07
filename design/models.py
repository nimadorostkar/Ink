from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=100,blank=True,null=True)
    description = models.CharField(max_length=700,blank=True,null=True)
    image = models.ImageField(upload_to='cat',default="cat/default.png")

    def __str__(self):
        return self.title



class Design(models.Model):
    title = models.CharField(max_length=200,null=True,blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    description = models.CharField(max_length=300,null=True,blank=True)
    image = models.ImageField(upload_to='designs',null=True,blank=True)
    portfolio_homepage = models.BooleanField(default=False)

    def __str__(self):
        return self.title