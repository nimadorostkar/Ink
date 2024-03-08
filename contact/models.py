from django.db import models


class ContactMessage(models.Model):
    STATUS = (('New', 'New'),('Read', 'Read'),('Closed', 'Closed'),)
    name = models.CharField(max_length=60,blank=True,null=True)
    email = models.CharField(max_length=80,blank=True,null=True)
    message = models.TextField(max_length=1000,blank=True,null=True)
    status = models.CharField(max_length=10, choices=STATUS,default='New')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name)
