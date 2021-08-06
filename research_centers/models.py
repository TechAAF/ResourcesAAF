from django.db import models
from ckeditor.fields import RichTextField
from cloudinary.models import CloudinaryField


class Research_Center(models.Model):
    name = models.CharField(max_length=250)
    logo = CloudinaryField('logo')
    image1 = CloudinaryField('image1', blank=True, null=True , help_text='<b style="color:green;font-size: 15px">*IMPORTANT* All three image should be of equal ratio (preffered: 3 x 2 )</b>')
    image2 = CloudinaryField('image2', blank=True, null=True)
    image3 = CloudinaryField('image3', blank=True, null=True)
    join_us = models.CharField(max_length=1000, blank=True, null=True)
    video = models.CharField("Embeded Url", max_length=500, blank=True, null=True, help_text='<b style="color:blue;font-size: 15px">Video that will we shown on join us card of center</b>')
    short_description = models.TextField(blank=True, null=True)
    info = RichTextField()

    def __str__(self):
        return self.name
        

class Activity(models.Model):
    title = models.CharField(max_length=200)
    image = CloudinaryField('image', blank=True, null=True)
    video = models.CharField(max_length=1000, blank=True, null=True, help_text='<b style="color:green;font-size: 12px">*IMPORTANT* Only add either Video link or Image, If you add both, only the image will be shown</b>')
    text = RichTextField()
    research_center = models.ForeignKey(Research_Center,on_delete=models.CASCADE)

    def __str__(self):
        return self.title
