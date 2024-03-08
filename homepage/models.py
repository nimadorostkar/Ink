from django.db import models


class HomepageInfo(models.Model):
    name = models.CharField(max_length=40)
    short_description = models.CharField(max_length=80)
    about_me = models.TextField(max_length=700)
    cv_file = models.FileField(upload_to='cv',default="cv/default.pdf")
    email = models.CharField(max_length=80,null=True,blank=True)
    phone = models.CharField(max_length=80,null=True,blank=True)
    address = models.CharField(max_length=80,null=True,blank=True)
    instagram_link = models.CharField(max_length=150,null=True,blank=True)
    facebook_link = models.CharField(max_length=150, null=True, blank=True)
    twitter_link = models.CharField(max_length=150, null=True, blank=True)
    telegram_link = models.CharField(max_length=150, null=True, blank=True)
    whatsapp_link = models.CharField(max_length=150, null=True, blank=True)
    my_img = models.ImageField(upload_to='my_img',default="my_img/default.png")
    background_img = models.ImageField(upload_to='background_img', default="background_img/default.png")

    def save(self, *args, **kwargs):
        if self.__class__.objects.count():
            self.pk = self.__class__.objects.first().pk
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.name) + ' | ' + str(self.short_description)


