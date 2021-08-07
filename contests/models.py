from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import Permission, User
from cloudinary.models import CloudinaryField

class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class Contest(models.Model):
    name = models.CharField(max_length=200)
    short_description = models.TextField("short description", max_length=250, blank=True, null=True, help_text='<b style="color:dodgerblue;font-size: 12px">Description of the card shown on all contests page. *MAX_Length = 250 characters"</b>')
    info = RichTextField("Information of Contest", null=True)
    image = CloudinaryField('image', blank=True, null=True)
    start_date = models.DateField()
    end_date = models.DateField()
    category = models.ManyToManyField(Category,blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Submission(models.Model):
    user_id= models.ForeignKey(User,on_delete=models.CASCADE, related_name="user_id")
    contest= models.ForeignKey(Contest,on_delete=models.CASCADE)
    caption=models.TextField(blank=True, null=True)
    likes=models.ManyToManyField(User, blank=True, null=True)
    image= models.TextField(blank=True, null=True)
    image_id=models.CharField(null=True,default="",max_length=200)
    # video_url=models.TextField(blank=True, null=True)
    status=models.BooleanField("Approved", default=False)
    

