from django.db import models
from ckeditor.fields import RichTextField
from cloudinary.models import CloudinaryField


class Category(models.Model):
    name = models.CharField(max_length = 50)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Course(models.Model):
    title = models.CharField(max_length=100)
    short_description = models.TextField(max_length=250, blank=True, null=True, help_text='<b style="color:dodgerblue;font-size: 12px">Description of the card shown on all courses page. *MAX_Length = 250 characters"</b>')
    playlist_id = models.CharField("Youtube playlist url", max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    image = CloudinaryField('image')
    category = models.ManyToManyField(Category, blank=True, null=True)

    def __str__(self):
        return self.title


    # @staticmethod
    # def getCourses():
    #     return Course.objects.all()
