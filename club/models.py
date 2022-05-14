from collections import UserDict
from lzma import MODE_NORMAL
from django.db import models
from pkg_resources import resource_filename
from django.contrib.auth.models import User 
# Create your models here.

class Meeting(models.Model):
    meetingtitle=models.CharField(max_length=255)
    meetingdate=models.DateField()
    meetingtime=models.CharField(max_length=255)
    meetinglocation=models.CharField(max_length=255)
    meetingagenda=models.TextField(null=True, blank=True)

    def __str__(self):
        return self.meetingtitle
    
    class Meta:
        db_table='meeting'

class MeetingMinutes(models.Model):
    meetingid=models.ForeignKey(Meeting, on_delete=models.DO_NOTHING)
    attendance=models.ManyToManyField(User)
    minutes=models.IntegerField()

    def __str__(self):
        return self.meetingid
    
    class Meta:
        db_table='meetingminutes'

class Resource(models.Model):
    resourcename=models.CharField(max_length=255)
    resourcetype=models.CharField(max_length=255)
    resourceurl=models.URLField() 
    dateentered=models.DateField()
    userid=models.ForeignKey(User, on_delete=models.CASCADE)
    resourcedescription=models.TextField()

    def __str__(self):
        return self.resourcename

    class Meta:
        db_table='resource'

class Event(models.Model):
    eventtitle=models.CharField(max_length=255)
    eventlocation=models.CharField(max_length=255)
    eventdate=models.DateField()
    eventtime=models.TimeField()
    eventdescription=models.TextField()

    def __str__(self):
        return self.eventtitle

    class Meta:
        db_table='event'