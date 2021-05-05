from django.db import models
from djongo import models
#from mongoengine import *


# Create your models here.



#
# class Universities(Document):
#     _id = ObjectIdField(required=True)
#     UNIname = StringField(required=True)
#     title = StringField(required=True)
#     address_time = StringField(required=True)
#     link = StringField(required=True)
#     application_deadline = StringField(required=True)
#     meta = {'collection': 'UNIJOBS'}

class University(models.Model):
    _id = models.AutoField(primary_key = True)
    #_id = ObjectIdField(required=True)
    UNIname = models.CharField(verbose_name='UNIname',max_length=128)
    title = models.CharField(verbose_name='title',max_length=128)
    address_time = models.CharField(verbose_name='address_time',max_length=128)
    link = models.CharField(verbose_name='link',max_length=128)
    application_deadline = models.CharField(verbose_name='application_deadline',max_length=128)
    class Meta:
        verbose_name = 'University'
        verbose_name_plural = 'University'
