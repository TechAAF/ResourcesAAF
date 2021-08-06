from django.db import models
from ckeditor.fields import RichTextField
from cloudinary.models import CloudinaryField

class Category(models.Model):
    name = models.CharField(max_length = 50)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name
    
    
class Career_Talk(models.Model):
    title = models.CharField(max_length = 200)
    description = RichTextField("Description", null = True)
    image = CloudinaryField('image', blank=True, null=True)
    embeded_video_link = models.TextField(blank=True, null=True, help_text='<b style="color:green;font-size: 12px">*IMPORTANT* Only add either Video link or Image, If you add both, only the image will be shown</b>')
    date_added = models.DateTimeField(auto_now_add = True)
    category = models.ManyToManyField(Category, blank=True, null=True)
    is_active = models.BooleanField(default = True)

    class Meta:
        verbose_name_plural = 'Career Talks'

    def __str__(self):
        return self.title