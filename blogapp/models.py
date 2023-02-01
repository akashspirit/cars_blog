from django.db import models
from cloudinary.models import CloudinaryField
# Create your models here.
class blog (models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = CloudinaryField('image')
    upload_by = models.CharField(max_length=255)
    
class feedback (models.Model):
    description = models.TextField()
    upload_by = models.CharField(max_length=255)

class profile(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    user = models.CharField(max_length=255)
    email = models.EmailField()
    profile_pic = CloudinaryField('image')
    about_me = models.TextField()