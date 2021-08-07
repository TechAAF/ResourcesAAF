from django.db import models
from ckeditor.fields import RichTextField
from cloudinary.models import CloudinaryField


class Research_Center(models.Model):
    name = models.CharField(max_length=250)
    logo = CloudinaryField('logo', blank=True, null=True)
    image1 = CloudinaryField('image1', blank=True, null=True , help_text='<b style="color:orange;font-size: 12px">*IMPORTANT* All three image should be of equal ratio (preffered: 3 x 2 )</b>')
    image2 = CloudinaryField('image2', blank=True, null=True)
    image3 = CloudinaryField('image3', blank=True, null=True)
    join_us = models.CharField("Join us link", max_length=1000, blank=True, null=True)
    video = models.CharField("Embeded Url", max_length=500, blank=True, null=True, help_text='<b style="color:dodgerblue;font-size: 12px">Video that will we shown on join us card of research center</b>')
    short_description = models.TextField(max_length=250, blank=True, null=True, help_text='<b style="color:dodgerblue;font-size: 12px">Description of the card shown on all research centre page. *MAX_Length = 250 characters"</b>')
    info = RichTextField()

    def __str__(self):
        return self.name
        

class Activity(models.Model):
    title = models.CharField(max_length=200)
    image = CloudinaryField('image', blank=True, null=True)
    video = models.TextField(blank=True, null=True, help_text='<b style="color:orange;font-size: 12px">*IMPORTANT* Only add either Video link or Image, If you add both, only the image will be shown</b>')
    short_description = models.TextField(max_length=250, blank=True, null=True, help_text='<b style="color:dodgerblue;font-size: 12px">Description of the card shown. *MAX_Length = 250 characters"</b>')
    text = RichTextField()
    research_center = models.ForeignKey(Research_Center,on_delete=models.CASCADE)

    def __str__(self):
        return self.title
