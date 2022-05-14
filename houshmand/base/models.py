from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class roadmaps(models.Model):
    idofroadmaps = models.CharField(max_length=20)
    nameoftopic = models.CharField(max_length=200)
    thumbnail = models.ImageField(upload_to="images", verbose_name="تصویر مقاله")
    nameofbtn = models.CharField(max_length=200)
    def __str__(self):
        return self.idofroadmaps
class films(models.Model):
    urlofmove = models.CharField(max_length=300)
    tpicofmove = models.CharField(max_length=200)
    namemove = models.CharField(max_length=200)
    def __str__(self):
        return self.tpicofmove
class Topic(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Room(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL , null=True)
    topics = models.ForeignKey(Topic, on_delete=models.SET_NULL , null=True)
    name = models.CharField(max_length=100)
    deprecation = models.TextField(null=True, blank=True,max_length=100)
    participants = models.ManyToManyField(User, related_name='participants',blank=True)
    updates = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-updates','-created']
    
    def __str__(self):
        return self.name
class Messages(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    body = models.TextField(max_length=120)
    updates = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-updates','-created']
    
    def __str__(self):
        return self.body[0:50]
        
class Articles(models.Model):
    STATUS_CHOICES = (
        ('d', 'پیش نویس'),
        ('p', 'منتشر کردن'),
    )
    title = models.CharField(max_length = 200, verbose_name="عنوان مقاله")
    slug = models.SlugField(max_length = 100, unique=True, verbose_name="آدرس مقاله")
    description = models.TextField(verbose_name="محتوا")
    thumbnail = models.ImageField(upload_to="images", verbose_name="تصویر مقاله")
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, verbose_name="وضعیت")
    class Meta:
        verbose_name = "مقاله"
        verbose_name_plural = "مقالات"
    def __str__(self):
        return self.title
    