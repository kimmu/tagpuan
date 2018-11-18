from django.core.validators import RegexValidator
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User




# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete="models.CASCADE")
    date_of_birth = models.DateField()
    phone_number = models.CharField(max_length=13, blank=True)
    #phone_regex = RegexValidator(regex=r'^\(?(?:\+62)(?:\d{2,3})?\)?[ .-]?\d{2,4}[ .-]?\d{2,4}[ .-]?\d{2,4}$',
                                 #message="Phone number must be entered in the format: '+639182541122'. Up to 15 digits allowed.")
    #phone_number = models.CharField(validators=[phone_regex], max_length=13, blank=True)  # validators should be a list


    def __str__(self):
        return self.user.username



class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete="models.CASCADE")
    category = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    post = models.TextField()
    landmark = models.CharField(max_length=50)
    post_timestamp = models.DateTimeField('post_timestamp', auto_now_add=True)
    #POST_TYPE_CHOICES = (('Lost', 'Lost'),('Found', 'Found'))
    post_type = models.CharField(max_length=50, blank=False, default="Lost")
    image = models.ImageField(upload_to='images', blank=True)

    def __str__(self):
        return self.title


class Tag(models.Model):
    tag_id = models.AutoField(primary_key=True)
    tag = models.CharField(max_length=200)

    def __str__(self):
        return self.tag

class Attach(models.Model):
    attach_id = models.AutoField(primary_key=True)
    tag_id = models.ForeignKey(Tag, on_delete=models.CASCADE)
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.tag_id)


class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.category


class Landmark(models.Model):
    landmark_id = models.AutoField(primary_key=True)
    landmark = models.CharField(max_length=50)

    def __str__(self):
        return self.landmark


class Lost(models.Model):
    lost_id = models.AutoField(primary_key=True)
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
         return str(self.post_id)


class Found(models.Model):
    found_id = models.AutoField(primary_key=True)
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
         return str(self.post_id)