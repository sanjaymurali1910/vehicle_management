from django.db import models

# Create your models here.


class batch(models.Model): 
    vnum = models.CharField(max_length=100, null=True)
    vtype = models.CharField(max_length=100, null=True)
    vmodel = models.CharField(max_length=100, null=True)
    vdes = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.vnum

class user_registration(models.Model):

    firstname = models.CharField(max_length=240, null=True)
    lastname = models.CharField(max_length=240, null=True)
    username = models.CharField(max_length=240, null=True)
    email = models.EmailField(max_length=240, null=True)
    photo = models.FileField(upload_to='images/', null=True, blank=True)
    password = models.CharField(max_length=240, null=True)
    status = models.CharField(max_length=240, null=True, default='user')


    def __str__(self):
        return self.firstname